# coding:shift-jis

# for�\�����t���O�ŕ��򂷂�ꍇ
# ���ٓ��̐H�ރf�[�^���烊�X�g�쐬
foodstuff = ["Banana","Mango","Fish","Carrot","cabbege"]

# �}���S�[���Ȃ����m�F����
flag_found = False  #�}���S�[���Ȃ������m�F����ϐ��B�����l�Ƃ���False��ݒ�
for food in foodstuff:  #food�Ƃ����ϐ��ɁAfoodstuff�̒l��1������B�J��Ԃ��̂��тɐV�����l������B
	if food == "Mango":
		flag_found = True
		break

if flag_found:
	print("�}���S�[�������Ă܂�")
else:
	print("����܂���")

