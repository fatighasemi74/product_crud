

class Product:

    products = []

    def __int__(self, product_id, category_id, title, short_description,
                description, slug, permalink, IsAvailable, sku, price,
                regular_price, sale_price, manage_stock, stock_quantity,
                IsVisible, date_created_gmt, date_modified_gmt):

        self.product_id = product_id
        self.category_id = category_id
        self.title = title
        self.short_description = short_description
        self.description = description
        self.slug = slug
        self.permalink = permalink
        self.IsAvailable = IsAvailable
        self.sku = sku
        self.price = price
        self.regular_price = regular_price
        self.sale_price = sale_price
        self.manage_stock = manage_stock
        self.stock_quantity = stock_quantity
        self.IsVisible = IsVisible
        self.date_created_gmt = date_created_gmt
        self.date_modified_gmt = date_modified_gmt

    def __repr__(self):
        pass

    def create(self):
        pass

    def read(self):
        pass

    def update(self):
        pass

    def delete(self):
        pass
