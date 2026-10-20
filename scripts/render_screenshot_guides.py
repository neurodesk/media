#!/usr/bin/env python3
"""Regenerate shared launcher click guides from one unmodified capture."""
from pathlib import Path
import json
import argparse
from PIL import Image,ImageDraw,ImageFont
ROOT=Path(__file__).resolve().parents[1]
FOLDER=ROOT/'screenshots/neurodesk'
GUIDES={
 'neurodesktop-launcher-desktop.png':[(1,(166,194,269,297),(217,329),(217,299)),(2,(284,194,387,297),(335,329),(335,299))],
 'neurodesktop-launcher-terminal.png':[(1,(520,194,624,297),(573,329),(573,299))],
 'neurodesktop-launcher-notebook.png':[(1,(166,562,269,665),(139,614),(164,614))],
}
def render(source, name, markers):
 try:font=ImageFont.truetype('DejaVuSans-Bold.ttf',18)
 except OSError:font=ImageFont.load_default(size=18)
 image=source.copy();draw=ImageDraw.Draw(image)
 for number,box,label,tip in markers:
   draw.rounded_rectangle(box,radius=4,outline='white',width=6)
   draw.rounded_rectangle(box,radius=4,outline='#e76f00',width=3)
   draw.line([label,tip],fill='white',width=6);draw.line([label,tip],fill='#e76f00',width=3)
   x,y=label;draw.ellipse((x-15,y-15,x+15,y+15),fill='#123c5a',outline='white',width=2)
   draw.text(label,str(number),font=font,anchor='mm',fill='white')
 image.quantize(colors=256,method=Image.Quantize.MEDIANCUT,dither=Image.Dither.NONE).save(FOLDER/name,optimize=True)
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
