from django.db import models


# 首页
class Main(models.Model):
    img = models.CharField(max_length=100)
    name = models.CharField(max_length=30)
    trackid = models.CharField(max_length=20)

    class Meta:
        abstract = True  # 抽象类，不会被生成表


# 首页-轮播
class MainWheel(Main):
    class Meta:
        db_table = "axf_wheel"


# 首页-导航
class MainNav(Main):
    class Meta:
        db_table = 'axf_nav'


# 首页-必购
class MainMustbuy(Main):
    class Meta:
        db_table = 'axf_mustbuy'


# 首页-shop
class MainShop(Main):
    class Meta:
        db_table = 'axf_shop'



'''
insert into axf_mainshow(
    trackid,name,img,
    categoryid,brandname,
    img1,childcid1,productid1,longname1,price1,marketprice1,
    img2,childcid2,productid2,longname2,price2,marketprice2,
    img3,childcid3,productid3,longname3,price3,marketprice3 ) 
    
  values(
    "21782","优选水果","http://img0.jpg",
    "103532","爱鲜蜂",
    "http://img01","103533","118824","爱鲜蜂·特小凤西瓜1.5-2.5kg/粒","25.80","25.8",
    "http://img01","103534","116950","蜂觅·越南直采红心火龙果350-450g/盒","15.3","15.8",
    "http://img01","103533","118826","爱鲜蜂·海南千禧果400-450g/盒","9.9","13.8");
    
'''
# 主要商品
class MainShow(Main):

    categoryid = models.CharField(max_length=20)
    brandname = models.CharField(max_length=20)

    img1 = models.CharField(max_length=200)
    childcid1 = models.CharField(max_length=20)
    productid1 = models.CharField(max_length=20)
    longname1 = models.CharField(max_length=50)
    price1 = models.CharField(max_length=20)
    marketprice1 = models.CharField(max_length=20)

    img2 = models.CharField(max_length=200)
    childcid2 = models.CharField(max_length=20)
    productid2 = models.CharField(max_length=20)
    longname2 = models.CharField(max_length=50)
    price2 = models.CharField(max_length=20)
    marketprice2 = models.CharField(max_length=20)

    img3 = models.CharField(max_length=200)
    childcid3 = models.CharField(max_length=20)
    productid3 = models.CharField(max_length=20)
    longname3 = models.CharField(max_length=50)
    price3 = models.CharField(max_length=20)
    marketprice3 = models.CharField(max_length=20)

    class Meta:
        db_table = 'axf_mainshow'


'''
insert into axf_foodtypes(
      typeid,typename,childtypenames,typesort
    )
  values("104749","热销榜","全部分类:0",1),
        ("104747","新品尝鲜","全部分类:0",2),
        ("103532","优选水果","全部分类:0#进口水果:103534#国产水果:103533",3),
        ("103581","卤味熟食","全部分类:0",4),
        ("103536","牛奶面包","全部分类:0#酸奶乳酸菌:103537#牛奶豆浆:103538#面包蛋糕:103540",5),
        ("103549","饮料酒水","全部分类:0#饮用水:103550#茶饮/咖啡:103554#功能饮料:103553#酒类:103555#果汁饮料:103551#碳酸饮料:103552#整箱购:104503#植物蛋白:104489#进口饮料:103556",6),("103541","休闲零食","全部分类:0#进口零食:103547#饼干糕点:103544#膨化食品:103543#坚果炒货:103542#肉干蜜饯:103546#糖果巧克力:103545",7),("103557","方便速食","全部分类:0#方便面:103558#火腿肠卤蛋:103559#速冻面点:103562#下饭小菜:103560#罐头食品:103561#冲调饮品:103563",8),("103569","粮油调味","全部分类:0#杂粮米面油:103570#厨房调味:103571#调味酱:103572",9),("103575","生活用品","全部分类:0#个人护理:103576#纸品:103578#日常用品:103580#家居清洁:103577",10),("104958","冰激凌","全部分类:0",11);
'''

# 商品类型
class FoodType(models.Model):
    typeid = models.CharField(max_length=20)
    typename = models.CharField(max_length=20)
    childtypenames = models.CharField(max_length=200)
    typesort = models.IntegerField(default=1)

    class Meta:
        db_table = 'axf_foodtypes'


'''
insert into axf_goods(
    productid,productimg,productname,productlongname,
    isxf,pmdesc,specifics,price,marketprice,
    categoryid,childcid,childcidname,dealerid,
    storenums,productnum) 
  values(
    "11951","1.jpg","","乐吧薯片鲜虾味50.0g",0,0,"50g",2.00,2.500000,
    103541,103543,"膨化食品","4858",200,4);
'''

# 商品
class Goods(models.Model):
    productid = models.CharField(max_length=20)
    productimg = models.CharField(max_length=200)
    productname = models.CharField(max_length=100)
    productlongname = models.CharField(max_length=200)

    isxf = models.IntegerField(default=0)
    pmdesc = models.IntegerField(default=0)
    specifics = models.CharField(max_length=20)
    price = models.FloatField()
    marketprice = models.FloatField()

    categoryid = models.CharField(max_length=20)
    childcid = models.CharField(max_length=20)
    childcidname = models.CharField(max_length=20)
    dealerid = models.CharField(max_length=20)
    storenums = models.IntegerField()
    productnum = models.IntegerField()

    class Meta:
        db_table = 'axf_goods'

class User(models.Model):
    name = models.CharField(max_length=20)
    password = models.CharField(max_length=50)
    email = models.EmailField(null=True,blank=True)
    icon = models.CharField(max_length=60,null=True,blank=True)
    sex = models.BooleanField(default=True)
    is_delete = models.BooleanField(default=False)

#购物车
class Cart(models.Model):
    user = models.ForeignKey(User)
    goods = models.ForeignKey(Goods)
    num = models.IntegerField(default=1)
    is_select = models.BooleanField(default=True)

#订单
class Order(models.Model):
    order_id = models.CharField(max_length=50, unique=True)
    order_createtime= models.DateTimeField(auto_now_add=True)
    order_price = models.FloatField(default= 0)
    #订单状态:0表示刚下单还未支付(待付款) 1表示:已付款(待收货) 2表示(待评价) 3 表示(交易完成)
    order_status = models.CharField(max_length=10, default=0)
    user = models.ForeignKey(User)

#订单中的商品
class OrderGoods(models.Model):
    goods = models.ForeignKey(Goods)
    order = models.ForeignKey(Order)
    num = models.IntegerField(default=1)
    price = models.FloatField()


class Getpwd(models.Model):

    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)



