class Unit:
    # ...
    def mvmntobjbfld(self, field, feld_1_param: int, field_2_param: int, d, fl: bool, cr: bool, points_per_action: int = 1):
        """Функция реализует перемещение юнита по полю. в качестве параметров принимает текущие координаты юнита, 
        направление его движеия, состояние не летит ли он, состояние не крадется ли он и базовый параметр скорости с 
        которым двигается юнит
        :param field: поле по которому перемещается юнит
        :param feld_1_param: x-координата юнита
        :param field_2_param: у- координата юнита
        :param d: направление перемещения
        :param fl: летит ли юнит
        :param cr: крадется ли юнит
        :param points_per_action: базовый параметр скорости
        """

        # одновременно эти события не должны происходить
        if fl and cr:
            raise ValueError('Рожденный ползать летать не должен!')

        if fl:
            points_per_action *= 1.2
            if d == 'UP':  
                new_y = field_2_param + points_per_action
                new_x = feld_1_param  
            elif d == 'DOWN': 
                new_y = field_2_param - points_per_action
                new_x = feld_1_param  
            elif d == 'LEFT': 
                new_y = field_2_param  
                new_x = feld_1_param - points_per_action
            elif d == 'RIGHT': 
                new_y = field_2_param  
                new_x = feld_1_param + points_per_action
        if cr:
            points_per_action *= 0.5
            if d == 'UP':  
                new_y = field_2_param + points_per_action  
                new_x = feld_1_param  
            elif d == 'DOWN':  
                new_y = field_2_param - points_per_action  
                new_x = feld_1_param  
            elif d == 'LEFT':  
                new_y = field_2_param  
                new_x = feld_1_param - points_per_action  
            elif d == 'RIGHT':  
                new_y = field_2_param  
                new_x = feld_1_param + points_per_action  

            field.set_unit(x=new_x, y=new_y, unit=self)

