from bank import Bank
from timezone import Timezone



x = Bank(10, 'Carllos', 'Eduardo',  'America/St_Johns', 100)

print("depositing...")
x.deposit(50)

print("trying to withdraw more than client balance has...")
x.withdraw(200)

y = Bank(10, 'Carllos', 'Eduardo', 'America/Sao_Paulo', 100)

print("checking clients code...")
y.check_code('D_10_2022-03-18 22:44:21_0')

print("printing full name....")
print(y.full_name)