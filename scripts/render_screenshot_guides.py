#!/usr/bin/env python3
"""Regenerate shared launcher click guides from one unmodified capture."""
from pathlib import Path
import json
import argparse
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'screenshots/neurodesk'
GUIDES={
 'neurodesktop-launcher-desktop.png':[(1,(182,194,283,297),(233,316),(233,299)),(2,(300,194,401,297),(351,316),(351,299))],
 'neurodesktop-launcher-terminal.png':[(1,(536,194,637,297),(587,316),(587,299))],
 'neurodesktop-launcher-notebook.png':[(1,(182,562,283,665),(155,614),(180,614))],
}
def render(source, name, markers):
 try:font=ImageFont.truetype('DejaVuSans-Bold.ttf',18)
 except OSError:font=ImageFont.load_default(size=18)
 image=source.copy();draw=ImageDraw.Draw(image)
 for number,box,label,tip in markers:
   draw.rounded_rectangle(box,radius=4,outline='white',width=6)
   draw.rounded_rectangle(box,radius=4,outline='#6aa329',width=3)
   draw.line([label,tip],fill='white',width=6);draw.line([label,tip],fill='#6aa329',width=3)
   x,y=label;draw.ellipse((x-15,y-15,x+15,y+15),fill='#456b1b',outline='white',width=2)
   left,top,right,bottom=draw.textbbox((0,0),str(number),font=font)
   draw.text((x-(left+right)/2,y-(top+bottom)/2),str(number),font=font,fill='white')
 image.save(FOLDER/name,format='PNG',optimize=True)
def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--source-dir',type=Path,help='Folder of fresh, unmarked menu captures; these working files are not committed.')
 parser.add_argument('--only',action='append',help='Refresh only this output filename; repeat for multiple guides.')
 args=parser.parse_args()
 source=Image.open(FOLDER/'neurodesktop-jupyter-launcher.png').convert('RGB')
 for name,markers in GUIDES.items():
  if not args.only or name in args.only:render(source,name,markers)
 if not args.source_dir:
  print('Launcher guides refreshed. Supply --source-dir to refresh menu/control guides.')
  return
 for guide in json.loads((ROOT/'scripts/screenshot-guides.json').read_text()):
  if args.only and guide['output'] not in args.only:continue
  source=Image.open(args.source_dir/guide['source']).convert('RGB')
  if guide.get('right_padding'):
   padded=Image.new('RGB',(source.width+guide['right_padding'],source.height),'white')
   padded.paste(source,(0,0));source=padded
  markers=[]
  for marker in guide['markers']:
   x,y,w,h=marker['target']
   markers.append((marker['number'],(x,y,x+w,y+h),tuple(marker['label']),tuple(marker['tip'])))
  render(source,guide['output'],markers)
if __name__=='__main__':main()
