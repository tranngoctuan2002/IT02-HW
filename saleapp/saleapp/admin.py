from saleapp.models import Category, Product
from saleapp import app, db
from flask_admin import Admin, BaseView, expose
from flask_admin.contrib.sqla import ModelView

admin = Admin(app=app, name='Quản trị cơ sở dữ liệu', template_mode='Bootstrap4')

class ProductView(ModelView):
    column_searchable_list = ['name']
    column_filters = ['name', 'price']
    column_exclude_list = ['image']
    column_details_list = True
    column_labels = {
        'name': 'Tên sản phẩm',
        'description': 'Mô tả',
        'price': 'Giá'
    }

class StatsView(BaseView):
    @expose('/')
    def index(self):
        return self.render('admin/stats.html')

admin.add_view(ModelView(Category, db.session, name='Danh mục'))
admin.add_view(ProductView(Product, db.session, name='Sản phẩm'))
admin.add_view(StatsView(name='Thống kê - báo cáo'))