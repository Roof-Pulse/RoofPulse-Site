let counter=0;
let alertActive=false;

// Revenue counter animation
setInterval(()=>{
  counter+=Math.floor(Math.random()*500)+200;
  document.getElementById("counter").innerText="$"+counter.toLocaleString();
},2000);

// Calculator + bar chart
function calculate(){
  let calls=document.getElementById('calls').value;
  let value=document.getElementById('value').value;
  let close=document.getElementById('close').value;
  let jobs=calls*(close/100);
  let weekly=jobs*value;
  let monthly=weekly*4;
  document.getElementById("result").innerText="Estimated lost revenue: $"+monthly.toLocaleString()+" per month";
  let percent=Math.min(monthly/200000*100,100);
  let bar=document.getElementById("barChartFill");
  if(!bar){bar=document.createElement("div");bar.id="barChartFill";document.getElementById("barChart").appendChild(bar);}
  bar.style.width=percent+"%";
}

// AI receptionist simulator
let aiScript=[
  "Incoming call...",
  "AI: Thanks for calling. Are you looking for a roof repair or estimate?",
  "Caller: Estimate.",
  "AI: What address is the property located at?",
  "Caller: 123 Oak Street.",
  "AI: Perfect. A roofer will contact you shortly."
];

function playSound(id){let s=document.getElementById(id);if(s){s.play();}}

function startDemo(){
  playSound('ring');
  let i=0;
  let interval=setInterval(()=>{
    playSound('beep');
    document.getElementById("ai").innerText=aiScript[i];i++;
    if(i>=aiScript.length){clearInterval(interval);}
  },2000);
}
function chooseOption(opt){
  document.getElementById("ai").innerText="Caller selected: "+opt;
  playSound('beep');
}

// Live missed call feed
function generateCall(){
  let names=["John","Mike","Sarah","Tom","Jessica","David"];
  let streets=["Oak St","Pine Rd","Maple Ave","Hill Dr","Cedar Ln"];
  let name=names[Math.floor(Math.random()*names.length)];
  let street=streets[Math.floor(Math.random()*streets.length)];
  let li=document.createElement("li");
  li.innerText="Missed call captured: "+name+" — "+street;
  document.getElementById("callFeed").prepend(li);
  playSound('beep');
}

// Lead capture + dashboard
function saveLead(){
  let name=document.getElementById("name").value;
  let phone=document.getElementById("phone").value;
  let address=document.getElementById("address").value;
  let leads=JSON.parse(localStorage.getItem("roofpulse_leads")||"[]");
  leads.push({name:name,phone:phone,address:address,time:new Date().toLocaleString()});
  localStorage.setItem("roofpulse_leads",JSON.stringify(leads));
  document.getElementById("leadStatus").innerText="Lead captured";
}
function loadLeads(){
  let leads=JSON.parse(localStorage.getItem("roofpulse_leads")||"[]");
  let table=document.getElementById("leadTable");
  table.innerHTML="";
  leads.forEach(l=>{
    let row=`<tr>
      <td>${l.name}</td>
      <td>${l.phone}</td>
      <td>${l.address}</td>
      <td>${l.time}</td>
    </tr>`;
    table.innerHTML+=row;
  });
}

// Storm / competitor alerts
function triggerAlert(){
  if(alertActive){document.getElementById("alertBox").innerText="No alerts right now.";alertActive=false;return;}
  let messages=["Storm calls incoming!","Competitor answered first!","High demand in your area!"];
  let msg=messages[Math.floor(Math.random()*messages.length)];
  document.getElementById("alertBox").innerText=msg;
  alertActive=true;
}