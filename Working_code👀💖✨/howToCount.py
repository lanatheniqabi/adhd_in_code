# how to calculate seconds in a year
spm = 60
mph = 60
hpd = 24
dpy = 365          # use 366 for leap years

sph = spm * mph      # 3600
spd  = sph * hpd        # 86400
spy = spd * dpy           # 31536000

print(spd)   # 3600
print(spd)    # 86400
print(spy)   # 31536000
