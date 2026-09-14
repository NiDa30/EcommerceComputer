USE master;
GO
IF EXISTS (SELECT name FROM sys.databases WHERE name = 'Store')
BEGIN
    ALTER DATABASE Store SET SINGLE_USER WITH ROLLBACK IMMEDIATE;
    DROP DATABASE Store;
END
GO
create database Store
GO
USE Store
GO

--DBCC USEROPTIONS
ALTER DATABASE Store SET READ_COMMITTED_SNAPSHOT ON
GO

CREATE TABLE User@ (
    UserId INT IDENTITY(1,1) PRIMARY KEY,
    RoleName NVARCHAR(10) NOT NULL DEFAULT 'User' CHECK (RoleName IN ('Admin', 'User', 'Employee')),
    Email VARCHAR(320) NOT NULL UNIQUE,
    Password VARCHAR(255) NOT NULL,
    PasswordChangedAt DATETIME2,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE()
)

CREATE TABLE UserDetail (
    UserId INT PRIMARY KEY FOREIGN KEY REFERENCES User@(UserId) ON DELETE CASCADE,
    Name NVARCHAR(50) NOT NULL,
	Gender BIT, -- 1: Nam | 0: Nữ
    Phone VARCHAR(11),
    Address NVARCHAR(MAX),
    DateOfBirth DATE,
)

CREATE TABLE Brand (
    BrandId INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL UNIQUE
)

CREATE TABLE Category (
    CategoryId INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL UNIQUE
)

CREATE TABLE Product (
    ProductId INT IDENTITY(1,1) PRIMARY KEY,
    Title NVARCHAR(255) NOT NULL,
    Stock INT NOT NULL,
    Price INT NOT NULL,
    PromoPrice INT,
    Description NVARCHAR(MAX),
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    UpdatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    BrandId INT FOREIGN KEY REFERENCES Brand(BrandId),
    CategoryId INT FOREIGN KEY REFERENCES Category(CategoryId)
)

CREATE TABLE Gallery (
    GalleryId INT IDENTITY(1,1) PRIMARY KEY,
    Thumbnail NVARCHAR(MAX),
    ProductId INT NOT NULL FOREIGN KEY REFERENCES Product(ProductId) ON DELETE CASCADE,
	IsPrimary BIT NOT NULL DEFAULT 0
)


CREATE TABLE Cart (
    UserId INT NOT NULL FOREIGN KEY REFERENCES User@(UserId),
    ProductId INT NOT NULL FOREIGN KEY REFERENCES Product(ProductId) ON DELETE CASCADE, -- Xóa sản phẩm sẽ xóa giỏ hàng liên quan
    Quantity INT NOT NULL DEFAULT 1,
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    PRIMARY KEY (UserId, ProductId)
)

CREATE TABLE Order@ (
    OrderId INT IDENTITY(1,1) PRIMARY KEY,
    Name NVARCHAR(50) NOT NULL,
	Phone VARCHAR(11) NOT NULL,
    Address NVARCHAR(MAX) NOT NULL,
    Note NVARCHAR(MAX),
    Status NVARCHAR(50),
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    UpdatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
    UserId INT FOREIGN KEY (UserId) REFERENCES User@(UserId)
)

CREATE TABLE OrderDetail (
    OrderId INT NOT NULL FOREIGN KEY REFERENCES Order@(OrderId),
    ProductId INT NOT NULL FOREIGN KEY REFERENCES Product(ProductId),
    Price INT NOT NULL,
    Quantity INT NOT NULL,
	PRIMARY KEY (OrderId, ProductId),
)

CREATE TABLE Review (
    UserId INT NOT NULL FOREIGN KEY REFERENCES User@(UserId) ON DELETE CASCADE,
    ProductId INT NOT NULL FOREIGN KEY REFERENCES Product(ProductId) ON DELETE CASCADE,
    Rating INT NOT NULL,
    Comment NVARCHAR(MAX),
    CreatedAt DATETIME2 NOT NULL DEFAULT GETDATE(),
	PRIMARY KEY (UserId, ProductId),
)

GO
CREATE TRIGGER Tri_AddProduct ON Product
AFTER INSERT
AS
BEGIN
	INSERT INTO Gallery (ProductId, IsPrimary)
	SELECT ProductId, 1 FROM inserted;
END
GO

CREATE TRIGGER Tri_AddUserDetail ON User@
AFTER INSERT
AS
BEGIN
	INSERT INTO UserDetail (UserId, Name)
	SELECT UserId, SUBSTRING(Email, 1, CHARINDEX('@', Email) - 1)
	FROM inserted;
END
GO

CREATE TRIGGER Tri_AddGallery ON Gallery
AFTER INSERT, UPDATE
AS
BEGIN
	DECLARE @ProductId INT = (SELECT TOP 1 ProductId FROM inserted)
	IF (SELECT COUNT(*) FROM Gallery WHERE IsPrimary = 1 AND ProductId = @ProductId) > 1
	BEGIN
		RAISERROR ('Each product can only have one primary image.', 16, 1);
		ROLLBACK TRANSACTION;
	END
END
GO




-- Thêm tài khoản người dùng (Mật khẩu mặc định: 123456)
INSERT INTO User@ (RoleName, Email, Password)
VALUES 
('Admin', 'admin1@example.com', '$2a$11$l55UTt/T80OfIKiF7vo6d.f7jXEVUlJbXcam6fFtzOs4rkBuCs3d2'),
('User', 'user1@example.com', '$2a$11$l55UTt/T80OfIKiF7vo6d.f7jXEVUlJbXcam6fFtzOs4rkBuCs3d2'),
('Employee', 'employee1@example.com', '$2a$11$l55UTt/T80OfIKiF7vo6d.f7jXEVUlJbXcam6fFtzOs4rkBuCs3d2'),
('Admin', 'admin2@example.com', '$2a$11$l55UTt/T80OfIKiF7vo6d.f7jXEVUlJbXcam6fFtzOs4rkBuCs3d2'),
('User', 'user2@example.com', '$2a$11$l55UTt/T80OfIKiF7vo6d.f7jXEVUlJbXcam6fFtzOs4rkBuCs3d2')

-- Thêm thương hiệu
INSERT INTO Brand (Name)
VALUES 
('Dell'),
('HP'),
('Asus'),
('Lenovo'),
('Acer')

-- Thêm danh mục sản phẩm
INSERT INTO Category (Name)
VALUES 
('Laptop'),
('Desktop'),
('Tablet'),
('Monitor'),
('Accessory')

-- Thêm sản phẩm
INSERT INTO Product (Title, Stock, Price, PromoPrice, Description, BrandId, CategoryId)
VALUES 
(N'Dell XPS 13', 10, 20000000, 18000000, N'Laptop Dell XPS 13 với thiết kế mỏng nhẹ', NULL, NULL),
(N'HP Pavilion', 15, 15000000, 14000000, N'Laptop HP Pavilion với hiệu năng cao', 2, 1),
(N'Asus ZenBook', 8, 18000000, 17000000, N'Laptop Asus ZenBook với hiệu suất mạnh mẽ', 3, 1),
(N'Lenovo ThinkPad', 12, 16000000, 15000000, N'Laptop Lenovo ThinkPad bền bỉ và hiệu quả', 4, 1),
(N'Acer Aspire', 20, 14000000, 13000000, N'Laptop Acer Aspire phù hợp cho học tập', 5, 1),
(N'Dell XPS 13 - Version 1', 10, 20000000, 18000000, N'Laptop Dell XPS 13 với thiết kế mỏng nhẹ', 1, 1),
(N'Dell XPS 13 - Version 2', 12, 21000000, 18500000, N'Laptop Dell XPS 13 bản nâng cấp', 1, 1),
(N'Dell XPS 13 - Version 3', 8, 19500000, 17500000, N'Laptop Dell XPS 13 bản mỏng nhẹ', 1, 1),
(N'Dell XPS 13 - Version 4', 15, 22000000, 20000000, N'Laptop Dell XPS 13 hiệu năng cao', 1, 1),
(N'Dell XPS 13 - Version 5', 9, 20500000, 19000000, N'Laptop Dell XPS 13 siêu di động', 1, 1),
(N'Dell XPS 13 - Version 6', 11, 20000000, 18500000, N'Laptop Dell XPS 13 bản đặc biệt', 1, 1),
(N'Dell XPS 13 - Version 7', 13, 21500000, 19500000, N'Laptop Dell XPS 13 với màn hình đẹp', 1, 1),
(N'Dell XPS 13 - Version 8', 7, 19000000, 17000000, N'Laptop Dell XPS 13 nhẹ nhàng và mạnh mẽ', 1, 1),
(N'Dell XPS 13 - Version 9', 14, 22500000, 20000000, N'Laptop Dell XPS 13 với viền màn hình siêu mỏng', 1, 1),
(N'Dell XPS 13 - Version 10', 10, 20000000, 18500000, N'Laptop Dell XPS 13 với hiệu suất tối ưu', 1, 1),
(N'Dell XPS 13 - Version 11', 10, 21000000, 18500000, N'Laptop Dell XPS 13 cho doanh nhân', 1, 1),
(N'Dell XPS 13 - Version 12', 8, 19500000, 17500000, N'Laptop Dell XPS 13 bản mỏng nhẹ hơn', 1, 1),
(N'Dell XPS 13 - Version 13', 15, 22000000, 20000000, N'Laptop Dell XPS 13 siêu bền', 1, 1),
(N'Dell XPS 13 - Version 14', 9, 20500000, 19000000, N'Laptop Dell XPS 13 cao cấp', 1, 1),
(N'Dell XPS 13 - Version 15', 11, 20000000, 18500000, N'Laptop Dell XPS 13 cho công việc và giải trí', 1, 1),
(N'Dell XPS 13 - Version 16', 13, 21500000, 19500000, N'Laptop Dell XPS 13 màn hình siêu sắc nét', 1, 1),
(N'Dell XPS 13 - Version 17', 7, 19000000, 17000000, N'Laptop Dell XPS 13 mạnh mẽ và thời trang', 1, 1),
(N'Dell XPS 13 - Version 18', 14, 22500000, 20000000, N'Laptop Dell XPS 13 với công nghệ tiên tiến', 1, 1),
(N'Dell XPS 13 - Version 19', 10, 20000000, 18500000, N'Laptop Dell XPS 13 bản nâng cao', 1, 1),
(N'Dell XPS 13 - Version 20', 12, 21000000, 18500000, N'Laptop Dell XPS 13 hiệu năng tuyệt vời', 1, 1)

-- Cập nhật hình ảnh sản phẩm chính (Thumbnail)
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13.jpg' WHERE ProductId = 1 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_hp_pavilion.jpg' WHERE ProductId = 2 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_asus_zenbook.jpg' WHERE ProductId = 3 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_lenovo_thinkpad.jpg' WHERE ProductId = 4 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_acer_aspire.jpg' WHERE ProductId = 5 AND IsPrimary = 1;

UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v1.jpg' WHERE ProductId = 6 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v2.jpg' WHERE ProductId = 7 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v3.jpg' WHERE ProductId = 8 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v4.jpg' WHERE ProductId = 9 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v5.jpg' WHERE ProductId = 10 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v6.jpg' WHERE ProductId = 11 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v7.jpg' WHERE ProductId = 12 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v8.jpg' WHERE ProductId = 13 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v9.jpg' WHERE ProductId = 14 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v10.jpg' WHERE ProductId = 15 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v11.jpg' WHERE ProductId = 16 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v12.jpg' WHERE ProductId = 17 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v13.jpg' WHERE ProductId = 18 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v14.jpg' WHERE ProductId = 19 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v15.jpg' WHERE ProductId = 20 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v16.jpg' WHERE ProductId = 21 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v17.jpg' WHERE ProductId = 22 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v18.jpg' WHERE ProductId = 23 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v19.jpg' WHERE ProductId = 24 AND IsPrimary = 1;
UPDATE Gallery SET Thumbnail = 'thumbnail_dell_xps_13_v20.jpg' WHERE ProductId = 25 AND IsPrimary = 1;

-- Thêm hình ảnh thư viện phụ
INSERT INTO Gallery (Thumbnail, ProductId, IsPrimary)
VALUES 
('gallery_dell_xps_13_1.jpg', 1, 0),	
('gallery_dell_xps_13_2.jpg', 1, 0),
('gallery_hp_pavilion_1.jpg', 2, 0),
('gallery_hp_pavilion_2.jpg', 2, 0),
('gallery_asus_zenbook_1.jpg', 3, 0),
('gallery_asus_zenbook_2.jpg', 3, 0),
('gallery_lenovo_thinkpad_1.jpg', 4, 0),
('gallery_lenovo_thinkpad_2.jpg', 4, 0),
('gallery_acer_aspire_1.jpg', 5, 0),
('gallery_acer_aspire_2.jpg', 5, 0)

GO
CREATE PROC AddCart @userId INT, @productId INT
AS
BEGIN
	DECLARE @num INT = (SELECT COUNT(*) FROM Cart WHERE UserId = @userId AND ProductId = @productId)
	IF @num = 0
	BEGIN
		DECLARE @result INT
		INSERT INTO Cart (UserId, ProductId, Quantity) VALUES (@userId, @productId, 1)
		SET @result = @@ROWCOUNT
		RETURN @result
	END
	ELSE
	BEGIN
		UPDATE Cart
		SET Quantity = Quantity + 1
		WHERE UserId = @userId AND ProductId = @productId
		RETURN 1
	END

END

