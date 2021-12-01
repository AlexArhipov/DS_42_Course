import os
import sys

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    try:
        if os.environ['VIRTUAL_ENV'] == "/Users/avivien/PycharmProjects/ex000/avivien":
            print("Виртуальная среда успешно запущена")
            s = "six == 1.14.0\nsoupsieve == 2.0\ntermgraph == 0.2.0\nwcwidth == 0.1.9\nzipp == 3.1.0"
            with open("requirements.txt", "w") as f:
                os.system("pip install -r requirements.txt --user")
                os.system("pip freeze")
                os.system("pip freeze > requirements.txt")
                # os.system("tar -zcvf avivien.tar.gz avivien")
    except:
        print('Виртуальная среда не запущена')
        sys.exit(1)
    # if os.system("echo Your current virtual env is $VIRTUAL_ENV") == "/Users/avivien/PycharmProjects/ex000/avivien":
    # s = os.environ.get("$PWD")