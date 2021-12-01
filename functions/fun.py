import math as m

input_angle = []
required_output = []
generated_output = []
error = []

for i in range(30, 120):
    if i % 10 == 0:
        input_angle.append(i)


def gen_values(x):
    angle_in_radians = m.radians(x)
    k1 = 0.402
    k2 = 0.402
    k3 = 1.012
    cos_x = m.cos(angle_in_radians)
    sin_x = m.sin(angle_in_radians)

    A = (1 - k2) * cos_x - k1 + k3
    B = -2 * sin_x
    C = k1 - (1 + k2) * cos_x + k3

    gen_value = 2 * m.atan((-B + m.sqrt(B * B - 4 * A * C)) / (2 * A))

    return m.degrees(gen_value).__round__(3)


for i in input_angle:
    required_output.append(((240 * (i - 7.5)) / (i + 60)).__round__(3))

for i in input_angle:
    generated_output.append((gen_values(i)).__round__(3))

for i in range(0, len(required_output)):
    error.append((required_output[i] - generated_output[i]).__round__(3))

for i in range(0, len(generated_output)):
    print(str(i + 1) + "       || " + str(input_angle[i]) + "     ||  " + str(required_output[i]) + "     ||    " + str(
        generated_output[i]) + "       ||  " + str(error[i]))
