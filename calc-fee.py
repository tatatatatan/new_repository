# coding:shift-jis

# ����V���n�̓��ꗿ���v�Z����v���O����
# �l���̓���
children = int(input("�q�������i�P�R�˖����j�͉��l�H"))
normal = int(input("�ʏ헿���i�P�R-�U�S�ˁj�͉��l�H"))
elder = int(input("�N�z�җ����i�U�T�ˈȏ�j�͉��l�H"))
# �W�v
total_num = children + normal + elder
children_price = children * 500
normal_price = normal * 1000
elder_price = elder * 700
total_price = children_price + normal_price + elder_price
# �����Ώۂ��m�F
if total_num >= 10:
	print("�c�̊���������܂�")
	total_price = total_price * 0.8
else:
	print("�c�̊����͂���܂���")
# ���ʂ�\��
print("�q�������@:{0}�l�~ 500= {1}�~".format(children,children_price))
print("�ʏ헿���@:{0}�l�~1000= {1}�~".format(normal,normal_price))
print("�N�z�җ���:{0}�l�~ 700= {1}�~".format(elder,elder_price))
print("���v:�@{0}�l�@{1}�~".format(total_num,total_price))
