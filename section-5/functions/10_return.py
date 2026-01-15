def chai_status (cups_ready):
    if cups_ready==0:
        return "no chai is ready"
    return f"{cups_ready} cups of chai are ready"


print(chai_status(0))
print(chai_status(10))


def multi_chai():
    return 20,30

cupp1,cup2=multi_chai()

print(cupp1,cup2)