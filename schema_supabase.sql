-- Script khởi tạo Database cho PostgreSQL (Tương thích pgAdmin & Supabase)
-- Chuyển đổi từ Store.sql (SQL Server T-SQL sang PostgreSQL)

-- 1. Bảng Người dùng (app_users)
CREATE TABLE IF NOT EXISTS app_users (
    user_id SERIAL PRIMARY KEY,
    role_name VARCHAR(10) NOT NULL DEFAULT 'User' CHECK (role_name IN ('Admin', 'User', 'Employee')),
    email VARCHAR(320) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    password_changed_at TIMESTAMP WITH TIME ZONE,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- 2. Chi tiết người dùng (user_details)
CREATE TABLE IF NOT EXISTS user_details (
    user_id INT PRIMARY KEY REFERENCES app_users(user_id) ON DELETE CASCADE,
    name VARCHAR(50) NOT NULL,
    gender BOOLEAN, -- true: Nam | false: Nữ
    phone VARCHAR(11),
    address TEXT,
    date_of_birth DATE
);

-- 3. Thương hiệu (brands)
CREATE TABLE IF NOT EXISTS brands (
    brand_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- 4. Danh mục (categories)
CREATE TABLE IF NOT EXISTS categories (
    category_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL UNIQUE
);

-- 5. Sản phẩm (products)
CREATE TABLE IF NOT EXISTS products (
    product_id SERIAL PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    stock INT NOT NULL DEFAULT 0,
    price INT NOT NULL DEFAULT 0,
    promo_price INT,
    description TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    brand_id INT REFERENCES brands(brand_id),
    category_id INT REFERENCES categories(category_id)
);

-- 6. Thư viện ảnh (galleries)
CREATE TABLE IF NOT EXISTS galleries (
    gallery_id SERIAL PRIMARY KEY,
    thumbnail TEXT,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    is_primary BOOLEAN NOT NULL DEFAULT FALSE
);

-- 7. Giỏ hàng (carts)
CREATE TABLE IF NOT EXISTS carts (
    user_id INT NOT NULL REFERENCES app_users(user_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    quantity INT NOT NULL DEFAULT 1,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, product_id)
);

-- 8. Đơn hàng (orders)
CREATE TABLE IF NOT EXISTS orders (
    order_id SERIAL PRIMARY KEY,
    name VARCHAR(50) NOT NULL,
    phone VARCHAR(11) NOT NULL,
    address TEXT NOT NULL,
    note TEXT,
    status VARCHAR(50) DEFAULT 'Pending',
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    user_id INT REFERENCES app_users(user_id)
);

-- 9. Chi tiết đơn hàng (order_details)
CREATE TABLE IF NOT EXISTS order_details (
    order_id INT NOT NULL REFERENCES orders(order_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    price INT NOT NULL,
    quantity INT NOT NULL,
    PRIMARY KEY (order_id, product_id)
);

-- 10. Đánh giá (reviews)
CREATE TABLE IF NOT EXISTS reviews (
    user_id INT NOT NULL REFERENCES app_users(user_id) ON DELETE CASCADE,
    product_id INT NOT NULL REFERENCES products(product_id) ON DELETE CASCADE,
    rating INT NOT NULL CHECK (rating BETWEEN 1 AND 5),
    comment TEXT,
    created_at TIMESTAMP WITH TIME ZONE NOT NULL DEFAULT CURRENT_TIMESTAMP,
    PRIMARY KEY (user_id, product_id)
);

-- TRIGGERS & FUNCTIONS (PostgreSQL Dialect)

-- Trigger tự tạo user_details khi thêm app_users
CREATE OR REPLACE FUNCTION fn_after_insert_user()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO user_details (user_id, name)
    VALUES (NEW.user_id, SPLIT_PART(NEW.email, '@', 1));
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tri_add_user_detail ON app_users;
CREATE TRIGGER tri_add_user_detail
AFTER INSERT ON app_users
FOR EACH ROW
EXECUTE FUNCTION fn_after_insert_user();

-- Trigger tự tạo gallery primary khi thêm product
CREATE OR REPLACE FUNCTION fn_after_insert_product()
RETURNS TRIGGER AS $$
BEGIN
    INSERT INTO galleries (product_id, is_primary)
    VALUES (NEW.product_id, TRUE);
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

DROP TRIGGER IF EXISTS tri_add_product ON products;
CREATE TRIGGER tri_add_product
AFTER INSERT ON products
FOR EACH ROW
EXECUTE FUNCTION fn_after_insert_product();

-- DỮ LIỆU MẪU (SEED DATA)
INSERT INTO app_users (role_name, email, password) VALUES 
('Admin', 'admin1@example.com', '$2y$10$f6aTCo72j1YVSnO2kYqSfu1twbdhZdU3qN3R6PWIQKPY99geHvVD.'),
('User', 'user1@example.com', '$2y$10$eo2MugDWT/NbZ9oNlhNFJOEhRtD9cVJc87//.pFJH3EDqZMuUMmza'),
('Employee', 'employee1@example.com', '$2y$10$3itQ6m7Z6NiYXMwln0HLpukKTCkyLkO3eTglR.F1Y6/C92ECBGWsC')
ON CONFLICT (email) DO NOTHING;

INSERT INTO brands (name) VALUES ('Dell'), ('HP'), ('Asus'), ('Lenovo'), ('Acer')
ON CONFLICT (name) DO NOTHING;

INSERT INTO categories (name) VALUES ('Laptop'), ('Desktop'), ('Tablet'), ('Monitor'), ('Accessory')
ON CONFLICT (name) DO NOTHING;

INSERT INTO products (title, stock, price, promo_price, description, brand_id, category_id) VALUES 
('Dell XPS 13', 10, 20000000, 18000000, 'Laptop Dell XPS 13 với thiết kế mỏng nhẹ', 1, 1),
('HP Pavilion', 15, 15000000, 14000000, 'Laptop HP Pavilion với hiệu năng cao', 2, 1),
('Asus ZenBook', 8, 18000000, 17000000, 'Laptop Asus ZenBook với hiệu suất mạnh mẽ', 3, 1),
('Lenovo ThinkPad', 12, 16000000, 15000000, 'Laptop Lenovo ThinkPad bền bỉ và hiệu quả', 4, 1),
('Acer Aspire', 20, 14000000, 13000000, 'Laptop Acer Aspire phù hợp cho học tập', 5, 1);
