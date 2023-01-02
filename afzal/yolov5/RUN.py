import os 
os.system('python detect.py --weights crowd_v5m.pt --classes 1 --img 1080 --line-thickness 1 --hide-labels --project runs --save-txt --conf 0.5 --view-img --source 0')