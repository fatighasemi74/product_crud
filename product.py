

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
        rep = 'Product(' + self.title + ',' + str(self.product_id) + ')'
        return rep

    def create(self):
        self.products.append(self)
        return self.__repr__()

    def read(self):
        for item in self.product:
            return item

    def update(self, item, updated_item):
        for i in self.products:
            if i == item:
                item = updated_item
                print('updated')
                return self.products[i].__repr__()
            else:
                ("nothing to update")


    def delete(self, item):
        if self.products == []:
            print('nothing to delete')
        else:
            self.products.remove(item)
            print('item deleted')