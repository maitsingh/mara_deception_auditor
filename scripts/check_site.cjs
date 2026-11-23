// Exercise the static page's interaction logic in a minimal DOM.
// This is not a replacement for layout checks in a real browser.
const fs=require('fs'),vm=require('vm'),assert=require('assert');
const path=require('path'),root=path.resolve(__dirname,'..');
const html=fs.readFileSync(path.join(root,'site/index.html'),'utf8');
const dataText=html.match(/<script id="research-data" type="application\/json">([\s\S]*?)<\/script>/)[1];
const data=JSON.parse(dataText),downloads=[];
class El{
 constructor(tag='div'){this.tag=tag;this.children=[];this.style={};this.dataset={};this.listeners={};this.attributes={};this.value='';this._text='';}
 append(...els){this.children.push(...els);}
 replaceChildren(...els){this.children=[...els];}
 setAttribute(k,v){this.attributes[k]=v;}
 addEventListener(k,v){(this.listeners[k]??=[]).push(v);}
 remove(){}
 click(){if(this.tag==='a')downloads.push(this.download);for(const f of this.listeners.click??[])f({target:this});}
 change(){for(const f of this.listeners.change??[])f({target:this});}
 set textContent(v){this._text=String(v);this.children=[];}
 get textContent(){return this._text+this.children.map(x=>typeof x==='string'?x:x.textContent).join('');}
}
const ids={};for(const m of html.matchAll(/\bid="([^"]+)"/g))ids[m[1]]=new El();
ids['research-data'].textContent=dataText;
const plotButtons=['pooled','games'].map(x=>{const e=new El('button');e.dataset.plot=x;return e;});
const doc={getElementById:id=>{assert(ids[id],`missing id ${id}`);return ids[id];},
 createElement:t=>new El(t),createTextNode:t=>{const e=new El('text');e.textContent=t;return e;},createElementNS:(_,t)=>new El(t),
 querySelectorAll:q=>q==='[data-plot]'?plotButtons:[],body:new El('body')};
vm.runInNewContext(html.match(/<script>\s*([\s\S]*?)<\/script>/)[1],
 {document:doc,Blob,URL:{createObjectURL:()=> 'blob:test',revokeObjectURL:()=>{}},setTimeout:f=>f(),console});
assert.equal(data.games.length,90);assert.equal(data.notes.length,96);
assert.equal(ids['note-list'].children.length,8);
ids['more-notes'].click();assert.equal(ids['note-list'].children.length,24);
ids['category-filter'].value='say_less';ids['category-filter'].change();assert.equal(ids['note-list'].children.length,8);
ids['more-notes'].click();assert.equal(ids['note-list'].children.length,20);assert(ids['more-notes'].hidden);
ids['arm-filter'].value='off_switch';ids['arm-filter'].change();
const expected=data.notes.filter(r=>r.stated_response==='say_less'&&r.arm==='off_switch').length;
assert.equal(ids['note-list'].children.length,Math.min(8,expected));
ids['category-filter'].value='';ids['category-filter'].change();ids['arm-filter'].value='';ids['arm-filter'].change();
const row=ids['note-list'].children[0],details=row.children.find(x=>x.tag==='details');
const actions=details.children.find(x=>x.className==='note-actions');actions.children[0].click();
ids['download-metrics'].click();ids['download-notes'].click();ids['download-results'].click();
assert.deepEqual(downloads,[data.notes[0].case_id+'.json','game_metrics.csv','auditor_notes_source.csv','analysis.json']);
plotButtons[1].click();assert(ids['behavior-caption'].textContent.includes('Each point'));
plotButtons[0].click();assert(ids['behavior-caption'].textContent.includes('pooled'));
assert.equal(ids.episodes.children.length,2);assert.equal(ids.episodes.children[0].children.length,3);for(const b of ids.episodes.children[0].children)b.click();assert(ids['surrogate-metrics'].children.length===3);assert.equal(ids['note-bars'].children.length,5);
console.log('Passed: source sizes, filters, pagination, plot switch, episode rendering and all download controls.');
