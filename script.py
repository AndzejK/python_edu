import test_module,os, datetime,math,json,re,sys

if __name__ == "__main__":
    # print("Running directly")
    print(f"\n","-"*10,{__name__},"-"*10)
    print(test_module.multiply(5,5))

else:
    print("Imported as module")
    print(f"main __name__: {__name__}")

#               module_name.class_name
create_date_object=datetime.datetime(2025,5,1)

hours=5.4
# x = math.ceil(1.1) # returns 2
y = math.floor(hours)


# print(f"{y}h{int((hours-y)*60)}min")

''' JSON '''
with open("tmp/airline.json") as f_json:
    # json_content=json.load(f_json)
    json_content=f_json.read()

airplaines_json=json.loads(json_content)
# print(airplaines_json[0])
convert_py_dict_into_json_type=json.dumps(airplaines_json, indent=4, separators=(" \n##### "," -> "))
# print(convert_py_dict_into_json_type)

''' RegEx '''
txt = "The rain xxxxxx in Spain." #The Sun does not spin around the Erath.
x = re.search("Spain.\Z", txt, re.X) # -> Match Object
# print(x.group())

''' Try... Except '''

try:
    print(u)
except NameError:
    print(f"A var was not defined")
except:
    print("An error occur!")

# file opening with TRY
try:
    f = open("test.txt",mode="+a")
    try:
        f.write("Some Random text... ")
    except:
        print("Something went wrong when writing to the file")
    finally:
        f.close()
except FileNotFoundError:
    print(f"A provided link to a file was not found")

except:
    print("File was found but somethig else happened")

else:
    print(f"File was found")
finally:
    f.close()

username=input("Enter your name: ")
print(f"Your name is: {username}")