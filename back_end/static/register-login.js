       function form_type(type){
        const form = document.getElementById(type+'-form')
         form.addEventListener('submit',async function postdata(e){
             e.preventDefault();
             const payload = new FormData(form);
             payload.append('type',type)
             const response =  await fetch('http://127.0.0.1:5000/reg',{method:'POST',body:payload});
             if (response.status===200){
                 if(document.getElementById('email_wrong')){
                     document.getElementById('email_wrong').remove();

                 }
                  const div = document.createElement('button');
                 div.className="btn btn-primary mb-2";
                 div.type = 'button';
                 div.disabled=true;
                 div.id ='successes'
                 const span = document.createElement('span');
                 span.role='status';
                 span.className="spinner-border spinner-border-sm";
                 const b = document.createElement('b');
                 b.textContent = " Successes"
                 div.append(span);
                 div.append(b)

                 if(type==='register'){
                    document.getElementById('up').append(div);
                 }else {
                    document.getElementById('in').append(div);
                 }

                 if(type==='register'){
                  setTimeout(function (){document.getElementById('switch').click(); document.getElementById('successes').remove();},1500)

                 }else {
              setTimeout(function (){location.href=response.url; document.getElementById('successes').remove();},1500)

                 }
                }
             else {
                 if(document.getElementById('email_wrong')){
                     document.getElementById('email_wrong').remove();

                 }
                 const json = await response.json();
                 const div = document.createElement('div');
                 div.className="alert alert-danger  text-center";
                 div.role = 'alert';
                 div.id='email_wrong';
                 div.textContent = json.message;
                 document.getElementById('main').append(div);
             }})}