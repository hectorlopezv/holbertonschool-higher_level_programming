#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    lista_ = [0] * list_length
    for idx in range(list_length):
        try:
            resu = my_list_1[idx] / my_list_2[idx]
        except ZeroDivisionError:
            print("division by 0")
            lista_[idx] = 0
        except IndexError:
            print("out of range")
        except (ValueError, TypeError):
            print("wrong type")
            lista_[idx] = 0
        else:
            lista_[idx] = resu
        finally:
            pass
    return lista_
