# coding:shift-jis

# BMI����v���O����
weight = float(input("�̏d(kg)�́H"))
height = float(input("�g��(cm)�́H"))
# BMI�̌v�Z
height = height / 100 # m�ɒ���
bmi = weight / (height * height)
# BMI�̒l�ɉ����Č��ʂ𕪐�
result = "" # result����ɂ��Ă���(������)
if bmi < 18.5:
	result = "�����^"
if ( 18.5 <= bmi < 25):
	result = "�W���̏d"
if (25 <= bmi < 30):
	result = "�얞(�y)"
if bmi >= 30:
	result = "�얞(�d)"
# ���ʂ�\��
print("BMI :", bmi)
print("����:", result)

