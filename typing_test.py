#!/usr/bin/env python3
"""typing_test - Typing analysis."""
import sys,argparse,json,random,time
WORDS="the quick brown fox jumps over lazy dog pack my box with five dozen liquor jugs how vexingly quick daft zebras jump".split()
def analyze_typing(target,typed):
    correct=sum(1 for a,b in zip(target,typed) if a==b)
    accuracy=correct/max(len(target),1)*100
    errors=len(target)-correct
    return {"target":target,"typed":typed,"accuracy":round(accuracy,1),"errors":errors,"length":len(target)}
def main():
    p=argparse.ArgumentParser(description="Typing test")
    p.add_argument("--words",type=int,default=20)
    p.add_argument("--analyze",nargs=2,metavar=("TARGET","TYPED"))
    args=p.parse_args()
    if args.analyze:
        print(json.dumps(analyze_typing(args.analyze[0],args.analyze[1]),indent=2))
    else:
        text=" ".join(random.choice(WORDS) for _ in range(args.words))
        print(json.dumps({"test_text":text,"word_count":args.words,"char_count":len(text)}))
if __name__=="__main__":main()
