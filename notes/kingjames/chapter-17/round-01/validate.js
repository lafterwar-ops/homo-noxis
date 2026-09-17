const fs = require('node:fs');
const crypto = require('node:crypto');
const path = require('node:path');
const baseline = fs.readFileSync(path.join(__dirname, 'baseline.tex'), 'utf8');
function wordCount(s) {
  return (s.replace(/^\\typesetchapter.*$/gm,'').replace(/^\\centerline.*$/gm,'').replace(/^\([^)]+\): --- /gm,'').replace(/\\(?:begin|end)\{[^}]+\}/g,'').replace(/\\[A-Za-z]+\*?(?:\[[^\]]*\])?/g,' ').match(/[A-Za-z0-9]+(?:['’\-][A-Za-z0-9]+)*/g)||[]).length;
}
const scripture = s => s.match(/\\begin\{scripture\}[\s\S]*?\\end\{scripture\}/g)||[];
for (const file of process.argv.slice(2)) {
 const raw=fs.readFileSync(file), text=raw.toString('utf8'), count=wordCount(text);
 const centers=text.split(/\r?\n/).filter(l=>l.includes('\\centerline'));
 const tokenStack=[]; const errors=[];
 for (const m of text.matchAll(/\\(begin|end)\{(room|scripture|declaration)\}/g)) { if(m[1]==='begin')tokenStack.push(m[2]); else if(tokenStack.pop()!==m[2])errors.push(m[0]); }
 console.log(JSON.stringify({file,sha256:crypto.createHash('sha256').update(raw).digest('hex').toUpperCase(),words:count,inBand:count>=3646&&count<=4456,centers:centers.length,nonEmptyCenters:centers.filter(l=>l.trim()!=='\\centerline{}'),anonymousTurns:(text.match(/^--- /gm)||[]).length,labelledTurns:(text.match(/^\([^)]+\): --- /gm)||[]).length,scriptureMatches:JSON.stringify(scripture(text))===JSON.stringify(scripture(baseline)),balanced:tokenStack.length===0&&errors.length===0}));
}

