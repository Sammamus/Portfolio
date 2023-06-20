from random import randint

def password_gen(word_count):
    try:
        if type(word_count) == int:

            full_password = []

            for word in range(word_count):

                word_build = []

                for i in range(5):
                    word_build.append(str(randint(1,6)))

                word_build = "".join(word_build)
                full_password.append(word_build)

            full_password = "-".join(full_password)
            
            print(full_password)

        else:
            raise Exception("word_count is not an integer")
    except Exception as e:
        print(e)

password_gen(5)