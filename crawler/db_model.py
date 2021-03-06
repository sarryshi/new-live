from peewee import *

database = MySQLDatabase('test_db2', **{'host': 'localhost', 'port': 3306, 'user': 'root', 'password': 'root123'})

class UnknownField(object):
    def __init__(self, *_, **__): pass

class BaseModel(Model):
    class Meta:
        database = database

class AuthGroup(BaseModel):
    name = CharField(unique=True)

    class Meta:
        db_table = 'auth_group'

class DjangoContentType(BaseModel):
    app_label = CharField()
    model = CharField()

    class Meta:
        db_table = 'django_content_type'
        indexes = (
            (('app_label', 'model'), True),
        )

class AuthPermission(BaseModel):
    codename = CharField()
    content_type = ForeignKeyField(db_column='content_type_id', rel_model=DjangoContentType, to_field='id')
    name = CharField()

    class Meta:
        db_table = 'auth_permission'
        indexes = (
            (('content_type', 'codename'), True),
        )

class AuthGroupPermissions(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')

    class Meta:
        db_table = 'auth_group_permissions'
        indexes = (
            (('group', 'permission'), True),
        )

class AuthUser(BaseModel):
    date_joined = DateTimeField()
    email = CharField()
    first_name = CharField()
    is_active = IntegerField()
    is_staff = IntegerField()
    is_superuser = IntegerField()
    last_login = DateTimeField(null=True)
    last_name = CharField()
    password = CharField()
    username = CharField(unique=True)

    class Meta:
        db_table = 'auth_user'

class AuthUserGroups(BaseModel):
    group = ForeignKeyField(db_column='group_id', rel_model=AuthGroup, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_groups'
        indexes = (
            (('user', 'group'), True),
        )

class AuthUserUserPermissions(BaseModel):
    permission = ForeignKeyField(db_column='permission_id', rel_model=AuthPermission, to_field='id')
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'auth_user_user_permissions'
        indexes = (
            (('user', 'permission'), True),
        )

class DjangoAdminLog(BaseModel):
    action_flag = IntegerField()
    action_time = DateTimeField()
    change_message = TextField()
    content_type = ForeignKeyField(db_column='content_type_id', null=True, rel_model=DjangoContentType, to_field='id')
    object = TextField(db_column='object_id', null=True)
    object_repr = CharField()
    user = ForeignKeyField(db_column='user_id', rel_model=AuthUser, to_field='id')

    class Meta:
        db_table = 'django_admin_log'

class DjangoMigrations(BaseModel):
    app = CharField()
    applied = DateTimeField()
    name = CharField()

    class Meta:
        db_table = 'django_migrations'

class DjangoSession(BaseModel):
    expire_date = DateTimeField(index=True)
    session_data = TextField()
    session_key = CharField(primary_key=True)

    class Meta:
        db_table = 'django_session'

class PublicDownloadAddress(BaseModel):
    create_time = DateTimeField()
    download_type = IntegerField()
    download_url = CharField()
    status = IntegerField()

    class Meta:
        db_table = 'public_download_address'

class ProductType(BaseModel):
    create_time = DateTimeField()
    describe = CharField(null=True)
    key = CharField()
    name = CharField()
    parent = IntegerField(db_column='parent_id')
    status = IntegerField()

    class Meta:
        db_table = 'product_type'

class PublicDataSource(BaseModel):
    create_time = DateTimeField()
    key = CharField()
    source_name = CharField()
    source_type = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'public_data_source'

class ProductInfo(BaseModel):
    create_time = DateTimeField()
    detail = IntegerField()
    order_index = IntegerField(null=True)
    product_name = CharField()
    product_type = ForeignKeyField(db_column='product_type_id', rel_model=ProductType, to_field='id')
    source = ForeignKeyField(db_column='source_id', rel_model=PublicDataSource, to_field='id')
    status = IntegerField()
    update_time = DateTimeField()

    class Meta:
        db_table = 'product_info'

class ProductDownloadDetail(BaseModel):
    address = ForeignKeyField(db_column='address_id', rel_model=PublicDownloadAddress, to_field='id')
    product = ForeignKeyField(db_column='product_id', rel_model=ProductInfo, to_field='id')

    class Meta:
        db_table = 'product_download_detail'

class PublicImages(BaseModel):
    create_time = DateTimeField()
    image = CharField()
    img_type = IntegerField()
    status = IntegerField()

    class Meta:
        db_table = 'public_images'

class ProductImagesDetail(BaseModel):
    image = ForeignKeyField(db_column='image_id', rel_model=PublicImages, to_field='id')
    product = ForeignKeyField(db_column='product_id', rel_model=ProductInfo, to_field='id')

    class Meta:
        db_table = 'product_images_detail'

class ProductMovieDetail(BaseModel):
    about = TextField(null=True)
    area = CharField(null=True)
    content = TextField(null=True)
    product_alias = CharField()
    product_name = CharField()
    rating = FloatField()
    rating_sum = IntegerField()
    release_time = DateField(null=True)
    status = IntegerField()

    class Meta:
        db_table = 'product_movie_detail'

class ProductSubTypeDetail(BaseModel):
    product = ForeignKeyField(db_column='product_id', rel_model=ProductInfo, to_field='id')
    sub_type = ForeignKeyField(db_column='sub_type_id', rel_model=ProductType, to_field='id')

    class Meta:
        db_table = 'product_sub_type_detail'

class SensitiveWords(BaseModel):
    word = CharField()
    word_type = IntegerField()

    class Meta:
        db_table = 'sensitive_words'

