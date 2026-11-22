import sys
sys.path.insert(0,'/home/user/work/build')
src=open('/home/user/work/build/make_prof.py').read()
# solo copertina + D0
exec(src.split("for name,a,b in SUB:")[0])
name,a,b='D0',0.0,57.6
d=nfr(b-a)/30;out=f'{B}/clips/D0.mkv'
fl=fade_list([[0,d,B+'/cover_b.png']],d);cc=f'{B}/clips/D0.txt';write_concat(fl,cc);compose(cc,a,a+d,None,out);open(out+'.ok','w').write('1');print('D0 ok')
