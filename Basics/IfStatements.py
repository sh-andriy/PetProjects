
is_male = False
is_tall = False

#if is_male or is_tall: # Це True якщо одна або дві змінні правдиві #
   #print("You are a male or tall or both")
#else:
    #print("You neither male nor tall")


if is_male and is_tall: # дві змінні мають бути правдиві #
    print("You are a tall male")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and is_tall:
    print("You are not a male but are tall")
else:
    print("You are not a male and not tall stupiid")
