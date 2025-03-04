from find_ft_type import all_thing_is_obj, all_thing_is_obj_isInstance, all_thing_is_obj_type

ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello": "titi!"}

# without any function
all_thing_is_obj(ft_list)
all_thing_is_obj(ft_tuple)
all_thing_is_obj(ft_set)
all_thing_is_obj(ft_dict)
all_thing_is_obj("Brian")
all_thing_is_obj("Toto")
print(all_thing_is_obj(10))

# with isInstance
all_thing_is_obj_isInstance(ft_list)
all_thing_is_obj_isInstance(ft_tuple)
all_thing_is_obj_isInstance(ft_set)
all_thing_is_obj_isInstance(ft_dict)
all_thing_is_obj_isInstance("Brian")
all_thing_is_obj_isInstance("Toto")
print(all_thing_is_obj_isInstance(10))

# with type
all_thing_is_obj_type(ft_list)
all_thing_is_obj_type(ft_tuple)
all_thing_is_obj_type(ft_set)
all_thing_is_obj_type(ft_dict)
all_thing_is_obj_type("Brian")
all_thing_is_obj_type("Toto")
print(all_thing_is_obj_type(10))
