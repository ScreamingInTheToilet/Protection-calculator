class Armor:

    def __init__(self, armor_points, enchantment_protection, Toughness_points, damage):
        self.armor_points = float(armor_points)
        self.enchantment_protection = float(enchantment_protection)
        self.Toughness_points = float(Toughness_points)
        self.damage = float(damage)
    
    def damage_reduction(self):
        Base_prot = self.armor_points * 0.04
        Tough_percentage = self.Toughness_points * 0.001

        Base_damage_reduction = (Base_prot - (0.008 - Tough_percentage)* self.damage)
        External = (1 - Base_damage_reduction) * self.enchantment_protection

        return Base_damage_reduction + External
    
    def leaked_damage(self):
        return self.damage - self.damage_reduction() * self.damage
    
    def armor_detection(self):
        list = [{'Armor': 'Netherite', 'Data':[20.0, 3.0]},{'Armor': 'Diamond', 'Data':[20.0, 2.0]},
                {'Armor': 'Iron', 'Data': [15.0, 0.0]},{'Armor': 'Chainmail', 'Data':[12.0, 0.0]},
                {'Armor': 'Gold', 'Data':[11.0, 0.0]},{'Armor': 'Leather', 'Data':[7.0, 0.0]}
                ]
        for i in list:
            Armor = i['Armor']
            Data = i['Data']
            if self.armor_points == Data[0]:
                if self.Toughness_points == Data[1]:
                    return Armor
            else:
                continue
            
            
# list_key = ['armor', 'projectile']

# while True:
#     user = input('Type a command: ').lower()
    
#     for i in user.split():
#         if i == 'armor':
#             armor = input('(Base defense point) (Enchantment protection) (Toughness point) (Damage inflicted)')
#             armor = Armor(armor.split()[0], armor.split()[1], armor.split()[2], armor.split()[3])
#             print(f'Damage reduction based on infliction: {round(armor.damage_reduction() * 100, 2)} percent')
#             print(f'Remaining vulnerability based on infliction: {round(armor.leaked_damage(), 1)} attack damage')
#             print(f'Armor detected: {armor.armor_detection()}')










# def damage_reduction(Armor_points, Toughness_points, external_protection, dam):
#     Base_prot = Armor_points * 0.04
#     Tough_percent = Toughness_points * 0.002

#     result = (Base_prot - (0.008 - Tough_percent) * dam) + (1 - (Base_prot-(0.008 -Tough_percent)*dam)) * external_protection

#     return result


