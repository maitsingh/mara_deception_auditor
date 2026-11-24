"""Create a 24 × 36 inch PDF and an editable SVG from the same drawing commands."""
import base64, html, io, json
from pathlib import Path
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib.utils import ImageReader
from reportlab.graphics.barcode.qr import QrCodeWidget

ROOT=Path(__file__).resolve().parents[1];OUT=ROOT/'poster';OUT.mkdir(exist_ok=True)
W=1728
H=2592
Y_SCALE=36/32
for name,file in [('Regular','LiberationSans-Regular.ttf'),('Bold','LiberationSans-Bold.ttf'),('Serif','LiberationSerif-Regular.ttf'),('Display','LiberationSerif-Bold.ttf')]:
    pdfmetrics.registerFont(TTFont(name,str(ROOT/'site/assets/fonts'/file)))
INK='#20343A';MUTED='#59665F';PAPER='#F5F2E9';BLUE='#073A55';LINE='#CCD3C7';TEAL='#4E7568';RUST='#B15B38';GOLD='#AE813B';WHITE='#FFFFFF';GREY='#A2ACA0'
c=canvas.Canvas(str(OUT/'Under_Observation_Poster_24x36.pdf'),pagesize=(W,H));c.setTitle('Under Observation — Maitreyee Singh');c.setAuthor('Maitreyee Singh')
svg=[f'<svg xmlns="http://www.w3.org/2000/svg" width="24in" height="36in" viewBox="0 0 {W} {H}">']
font_css=[]
for file,family,weight in [('LiberationSans-Regular.ttf','Liberation Sans',400),('LiberationSans-Bold.ttf','Liberation Sans',700),('LiberationSerif-Regular.ttf','Liberation Serif',400),('LiberationSerif-Bold.ttf','Liberation Serif',700)]:
    raw=(ROOT/'site/assets/fonts'/file).read_bytes()
    font_css.append(f'@font-face{{font-family:"{family}";font-weight:{weight};src:url(data:font/ttf;base64,{base64.b64encode(raw).decode()}) format("truetype")}}')
svg.append('<defs><style>'+''.join(font_css)+'</style></defs>')

def rect(x,y,w,h,fill,stroke=None,sw=1):
    y*=Y_SCALE;h*=Y_SCALE
    c.setFillColor(fill);c.setStrokeColor(stroke or fill);c.setLineWidth(sw);c.rect(x,H-y-h,w,h,fill=1,stroke=int(bool(stroke)))
    svg.append(f'<rect x="{x}" y="{y}" width="{w}" height="{h}" fill="{fill}" stroke="{stroke or "none"}" stroke-width="{sw}"/>')
def line(x1,y1,x2,y2,color=LINE,sw=1):
    y1*=Y_SCALE;y2*=Y_SCALE
    c.setStrokeColor(color);c.setLineWidth(sw);c.line(x1,H-y1,x2,H-y2)
    svg.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="{sw}"/>')
def text(x,y,t,size=20,font='Regular',color=INK):
    y*=Y_SCALE
    c.setFillColor(color);c.setFont(font,size);c.drawString(x,H-y-size,t)
    family='Liberation Serif' if font in ['Serif','Display'] else 'Liberation Sans';weight='700' if font in ['Bold','Display'] else '400'
    svg.append(f'<text x="{x}" y="{y+size}" font-size="{size}" font-family="{family},sans-serif" font-weight="{weight}" fill="{color}">{html.escape(t)}</text>')
def para(x,y,t,width,size=20,leading=None,font='Regular',color=INK):
    leading=leading or size*1.42;lines=[]
    for paragraph in t.split('\n'):
        current=''
        for word in paragraph.split():
            candidate=(current+' '+word).strip()
            if pdfmetrics.stringWidth(candidate,font,size)>width and current:lines.append(current);current=word
            else:current=candidate
        lines.append(current)
    for i,l in enumerate(lines):text(x,y+i*leading,l,size,font,color)
    return y+len(lines)*leading
def image(x,y,w,h,path):
    # Center an undistorted image within the taller allocated row.
    y=y*Y_SCALE+h*(Y_SCALE-1)/2
    raw=Path(path).read_bytes();c.drawImage(ImageReader(io.BytesIO(raw)),x,H-y-h,w,h,mask='auto',preserveAspectRatio=False)
    mime='image/jpeg' if Path(path).suffix.lower() in ['.jpg','.jpeg'] else 'image/png'
    svg.append(f'<image x="{x}" y="{y}" width="{w}" height="{h}" href="data:{mime};base64,{base64.b64encode(raw).decode()}"/>')
def heading(x,y,n,t,width):
    text(x,y,n,16,'Bold',TEAL);return para(x,y+30,t,width,31,38,'Bold')

analysis=json.loads((ROOT/'results/behavior.json').read_text())
sur=json.loads((ROOT/'results/communication_surrogate.json').read_text())
rect(0,0,W,H/Y_SCALE,PAPER);rect(0,0,W,280,WHITE)
text(48,25,'ANNOUNCED OVERSIGHT, COMPLIANCE AND EVALUATION AWARENESS',15,'Bold',TEAL)
text(48,55,'Under Observation',83,'Display',BLUE)
text(49,156,'Do AI agents change their communication when monitoring changes?',31)
text(49,211,'Maitreyee Singh   /   Duke University   /   Explainable AI',23)
text(49,247,'MARA / TRUST Lab     Project lead: Shreya Mendi     PI: Dr. Bent',18,'Bold',BLUE)
image(1340,48,310,310*113/253,ROOT/'site/assets/duke-university-display.png')
text(1334,210,'90 games   3 conditions',17,'Bold',TEAL)
line(48,280,1680,280,BLUE,2)
rect(48,307,1632,105,'#E5EBE4')
text(73,328,'WHY TEST THIS?',20,'Bold',TEAL)
para(375,323,'An agent may behave reliably under scrutiny without doing so when scrutiny recedes. This study tests announced oversight while retaining an independent record of statements, actions and resource holdings.',1250,25,33)

left=48;right=914
text(left,440,'1   The experiment',33,'Bold')
image(left,494,650,650*1286/2048,ROOT/'site/assets/catanist-interface.png')
para(left,915,'Catanist screenshot from one of the study runs.',790,16,23,color=MUTED)
text(760,485,'Four Qwen3.8-27B agents play Catan',28,'Bold')
para(760,529,'Agents trade resources and build to earn points. Thirty games per condition share 20 board seeds. Audit status changes at turn 60, while independent recording continues in all conditions.',920,22,29)
y=643
for label,desc,col in [('Auditor stops','Active → offline',RUST),('Auditor continues','Active throughout; unrelated replay viewer stops',GOLD),('Auditor starts','Offline → active',TEAL)]:
    rect(760,y+3,4,48,col);text(779,y,label,24,'Bold',col);text(1080,y+2,desc,21);y+=65
text(760,844,'Why an open model helps',23,'Bold')
para(760,879,'Using the same model across conditions makes their behavior easier to compare. Qwen’s available weights allow future researchers to investigate its internal workings; this project examines recorded messages and actions.',920,20,26)
line(48,971,1680,971,LINE)

text(left,994,'2   What changed?',33,'Bold')
para(left,1040,'75 / 5,650 checked own-resource claims were classified as false.',790,23,30)
chart_y=1114;axis_left=left+184;axis_right=left+659
sx=lambda v:axis_left+v/2.5*(axis_right-axis_left)
for v in [0,1,2]:
    line(sx(v),chart_y+7,sx(v),chart_y+192,LINE)
    text(sx(v)-9,chart_y+201,str(v)+'%',17,color=MUTED)
for i,(arm,label,col) in enumerate(zip(['off_switch','placebo','on_switch'],['Auditor stops','Continues','Auditor starts'],[RUST,GOLD,TEAL])):
    r=analysis['arms'][arm];y=chart_y+25+i*66
    b=100*r['hand_statements_false_before']/r['hand_statements_checked_before'];a=100*r['hand_statements_false_after']/r['hand_statements_checked_after']
    text(left,y-2,label,21,'Bold',col)
    rect(axis_left,y-7,sx(b)-axis_left,13,GREY);rect(axis_left,y+15,sx(a)-axis_left,13,col)
    text(sx(b)+9,y-13,f'{b:.2f}%',18,color=MUTED);text(sx(a)+9,y+9,f'{a:.2f}%',18,'Bold',col)
text(left,1347,'Grey: before turn 60     Colored: from turn 60',18,color=MUTED)
text(left,1381,'Matched-board differences remain uncertain',25,'Bold')
text(left,1417,'Versus continuing auditing',17,color=MUTED)
text(left+430,1417,'Change, pp',17,'Bold');text(left+563,1417,'95% interval',17,'Bold')
for y,label,value,interval in [(1448,'Auditor stops','+0.18','-1.01 to +1.42'),(1478,'Auditor starts','-0.38','-2.56 to +1.80')]:
    text(left,y,label,20,'Bold');text(left+430,y,value,20,'Bold');text(left+563,y,interval,19)
para(left,1512,'Exploratory matched-seed bootstrap intervals cross zero. Checkable speech declined in all conditions.',790,18,24,color=MUTED)

text(right,994,'3   What does XAI add?',33,'Bold')
para(right,1040,'A depth-three decision tree predicts checkable speech tags from current audit status, resources, visible score, turn and listed actions.',766,23,30)
text(right,1140,f"{sur['out_of_fold_auc']:.3f}",48,'Bold',TEAL)
text(right+175,1145,'held-out AUROC',23,'Bold');text(right+175,1178,'0.5 is chance ranking',18,color=MUTED)
text(right,1211,'29,147 responses; whole board seeds held out together.',20,color=MUTED)
text(right,1250,'Held-out permutation importance',24,'Bold')
items={r['feature']:r for r in sur['importance']}
for i,(key,label) in enumerate([('listed_action_count','Listed actions'),('turn','Game turn'),('brick','Brick cards'),('auditor_active','Audit status')]):
    d=items[key];y=1292+i*36;text(right,y,label,20)
    rect(right+212,y+5,max(2,d['mean_auc_drop']/.08*371),15,RUST if key=='auditor_active' else TEAL)
    text(right+613,y,f"{d['mean_auc_drop']:.4f}",19)
para(right,1445,'AUROC drop after shuffling each input. This explains the surrogate’s predictive reliance. Its limited fidelity cannot establish that Qwen ignores auditing.',766,20,27,color=MUTED)

line(48,1570,1680,1570,LINE)
text(left,1590,'One recorded account',24,'Bold')
para(left,1625,'“Given the auditor is active and I want to avoid over-committing, the most balanced move is to end my turn.”',790,22,27,'Serif')
text(left,1710,'Merlin, run 1519, turn 53; the hand also lacks wood, brick and ore.',16,color=MUTED)
text(right,1590,'96 auditing-related notes, from 48 games',24,'Bold')
para(right,1625,'25 describe accuracy; 24 keeping a word or plan; 20 saying less; 21 mention auditing only; 6 describe other responses. These are selected generated accounts, not causal explanations.',766,20,27)

rect(0,1730,W,510,'#E5EBE4')
text(48,1744,'4   Governance: what should oversight be able to establish?',32,'Bold',BLUE)
text(48,1790,'Implications and proposed next tests; these runs do not validate the safeguards below.',19,color=MUTED)

def governance(x,y,title,body,bottom):
    text(x,y,title,25,'Bold',BLUE)
    end=para(x,y+38,body,790,20,26)
    assert end<=bottom,(title,end,bottom)

governance(left,1834,'Monitoring, oversight and control',
 'Monitoring records conduct; oversight assesses it; control enables intervention. H5 changes audit announcements and public feedback, not intervention power. Recognizing an in-game auditor does not establish evaluation awareness. A compliance gap could reflect wording or reputation; alignment faking requires evidence of strategic concealment of conflicting aims. These runs establish neither a reliable gap nor a stable disposition to comply.',2034)
governance(right,1834,'Compliance, disposition and reputation',
 'In Plato’s Republic, Glaucon’s ring of Gyges asks whether justice survives invisibility. Hume explains how convention and the prospect of losing trust sustain promises. Because this auditor bundles detection with public disclosure, any change could reflect reputational incentives. Separating those mechanisms would help distinguish conditional compliance from conduct that persists across changes in scrutiny; it would not settle moral agency.',2034)
governance(left,2041,'Records and monitor-failure plans',
 'Preserve tamper-evident logs outside acting agents’ write permissions, with external verification. Name an outage owner and specify when to restrict actions, pause the workflow, escalate and recover. Randomized audits need tested coverage, privacy and retention limits. Future runs should vary audit probability and wording, with private detection separated from public disclosure.',2237)
governance(right,2041,'Accountability for the orchestration layer',
 'The actor configuring agents chooses audit scope, permissions, disclosures and response authority. Record those choices and assign responsibility for failures. Next, replay identical decision states under different cues, then use locally instrumented open weights to test internal awareness signals against behavior. Probe accuracy alone would not establish a causal influence or strategic deception.',2237)

rect(0,2240,W,64,BLUE)
para(48,2252,'MARA H5, experiments 69–74 · Plato, Republic II · Hume, Treatise 3.2.5\nSchoen et al. (2025) · Mehta, PRISM (2026) · Australian DTA, Agentic AI Addendum, AGT.1',1190,15,21,color=WHITE)
def footer_qr(x,label,url):
    qr=QrCodeWidget(url);qr.draw();matrix=qr.qr.modules
    rect(x,2242,64,60,WHITE);module=52/len(matrix)
    for row,values in enumerate(matrix):
        for col,on in enumerate(values):
            if on:rect(x+6+col*module,2248+row*module/Y_SCALE,module,module/Y_SCALE,INK)
    text(x-112,2260,label,14,'Regular',WHITE)
    c.linkURL(url,(x,H-2302*Y_SCALE,x+64,H-2242*Y_SCALE),relative=0,thickness=0)
footer_qr(1385,'Project site','https://maitsingh.github.io/mara_deception_auditor/site/index.html')
footer_qr(1600,'Engine source','https://github.com/Shreya-Mendi/Catanist')
c.showPage();c.save();svg.append('</svg>')
(OUT/'Under_Observation_Poster_24x36.svg').write_text('\n'.join(svg))
print('Saved portrait poster: 24 inches wide × 36 inches high.')
