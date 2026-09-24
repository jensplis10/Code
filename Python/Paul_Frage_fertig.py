prior = "0"
variables = {"0": False, "1": False, "2": True}
x = input()
variables[x] = not variables[x]
prior = x
prior = int(prior)
while prior < 2:
    prior += 1
    prior = str(prior)
    variables[prior] = variables[x]
    prior = int(prior)
print(variables)
