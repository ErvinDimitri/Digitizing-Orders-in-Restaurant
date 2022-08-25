/*Modal */
function changeB(op){
	op.addClass('active');
}
function aaa(){
  alert('a');
}
function addForm(val,id){
  var counter = 0;
  var btn = document.getElementById(id);
  var div = document.getElementById('pedidos');
  const queryS=window.location.search;
  const urlParams=new URLSearchParams(queryS);
  const mesa=urlParams.get('mesa');
  counter++;
  var label=document.createElement("label");
  label.id =val;
  label.name=val;
  label.className='itempedido';
  label.innerHTML=val;
  var input = document.createElement("input");
  input.id = 'input-' + counter;
  input.type = 'number';
  input.min='0';
  input.name = val+'_'+mesa;
  input.className='qty';
  input.maxLength=2;
  input.placeholder = 'quant';
  input.required=true;
  var divPed=document.createElement("div");
  divPed.className='pedido';
  divPed.id =val+'-div';
  var deleteBtn=document.createElement("button");
  deleteBtn.id=val+'-btn';
  deleteBtn.innerHTML='&times;';
  deleteBtn.addEventListener('click',function(){
    var item=deleteBtn.id.split("-")[0];
    var divDel=document.getElementById(item+'-div');
    divDel.remove();
    checkPed(val,id);
});
    deleteBtn.className='deletebtn';
    divPed.appendChild(label);
    divPed.appendChild(input);
    divPed.appendChild(deleteBtn);
    div.appendChild(divPed);
    try{document.appendChild(divPed);}
    catch(err){var a=5;}
    }

function createBtn(val,id){
  var btn=document.getElementById(id);
  btn.remove();
  var newBtn=document.createElement("button");
  var div=document.getElementById(id+'-card');
    div.innerHTML+='<button class="adicionar" value="'+val+'" id="'+id+'" onclick="changeV(value,id)">Adicionar</button>';
}

function checkPed(val,id){
  var t=document.getElementById("pedidos").querySelectorAll(".pedido");
  var pross=document.getElementById("prosseguir");
  createBtn(val,id);
    if (!t[0]){
      
      pross.style.display="none";
      modal.style.display ="none";
    }else{
      pross.innerHTML="prosseguir ("+t.length+")";
    }
}
function changeV(val,id){
	
  var div=document.getElementById(val+'-div');
  var btn=document.getElementById(id);
  if (div){
    btn.style.background='#06ac0c';
    btn.innerHTML="Adicionar";
    div.remove();
    checkPed(val,id);
  }else{
    const queryS=window.location.search;
    const urlParams=new URLSearchParams(queryS);
    const mesa=urlParams.get('mesa');
    if(mesa==null){alert('Para fazer o pedido, scaneie o codigo da sua mesa');}
    else{
      if (!mesa.startsWith("mesa")){
        alert('Para fazer o pedido, scaneie o codigo da sua mesa');
      }else{
        var pross=document.getElementById("prosseguir");
        pross.style.display="inline-block";  
        var t=document.getElementById("pedidos").querySelectorAll(".pedido");
        pross.innerHTML="prosseguir ("+(t.length+1)+")";
        btn.style.background='#035e06';
        btn.innerHTML="Adicionado";
        addForm(val,id); 
    
    }
  }
  }
}
  function submitMsg(){
    alert('Pedido requisitado com sucesso');
    //return true;
  }
	



const form=document.querySelector('form');
const sMsg = document.querySelector('success');
form.addEventListener('Submit', (e) => {
  e.preventDefault();
  sMsg.classList.add('show');
  setTimeout(() => form.submit(), 2000);
})


// Get the modal
var modal = document.getElementById("myModal");

// Get the button that opens the modal
var btn = document.getElementById("prosseguir");

// Get the <span> element that closes the modal
var span = document.getElementsByClassName("close")[0];

function f1() {
	var modal = document.getElementById("myModal");
  modal.style.display = "block";
}

// When the user clicks on <span> (x), close the modal
function f2() {
	var modal = document.getElementById("myModal");
  modal.style.display = "none";
}
function f3(event) {
	var modal = document.getElementById("myModal");
  if (event.target == modal) {
    modal.style.display = "none";
  }
}


function openNav() {
  document.getElementById("mySidenav").style.width = "250px";
}

function closeNav() {
  document.getElementById("mySidenav").style.width = "0";
}