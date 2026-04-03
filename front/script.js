//portfolio
//handle: _MUMINUL__ISLAM___

//CODE

let products_database=[];
let serached_product;
let job_result_list=[];
let cache_list=[];

const table_head=document.getElementById('list_table_head');
const table_body=document.getElementById('list_table');

async function fetch_database(){
    try{
        const response=await fetch('/backend/');
        const data=await response.json();
        products_database=data;
    }catch(err){
        console.error(err);
    }
}
fetch_database();

function add_product(product_id,product_name,product_model,product_core){

        const tr=document.createElement("tr");
        tr.innerHTML = `
                <td>${product_name}</td>
                <td>${product_model}</td>
                <td>${product_core}</td>
                <td><button class="add_remove_cart_btn" id=${product_id} onclick="toggle_button(this)" >Add</button>
        `;
        document.getElementById("list_table").appendChild(tr);

}


function search_database() {
    const base_URL="/backend/search/";
    const search_box=document.getElementById("search_box");

    search_box.addEventListener("keydown",(event_enter)=>{
        if(event_enter.key==="Enter"){
            event_enter.preventDefault();

            const search_term=encodeURIComponent(search_box.value.trim());
            const full_url=base_URL+search_term;

            async function search(url){
                try{
                    const search_response=await fetch(url);
                    if(search_response.ok){
                        const search_data=await search_response.json();
                        serached_product=search_data;

                        table_body.innerHTML="";
                        table_head.innerHTML="";

                        const tr=document.createElement('tr');
                        tr.innerHTML=`
                            <th>Product Name</th>
                            <th>Product Model</th>
                            <th>Product Core</th>
                        `
                        table_head.appendChild(tr);

                        add_product(serached_product.product_id,serached_product.product_name,serached_product.product_model,serached_product.product_core);
                    }
                    if(!search_response.ok){
                        alert(`Try after Time Limit`)
                    }
                }catch(err){
                    console.log("network error happened ")
                }
            }
            search(full_url);
        }
    });
}
search_database();

function show_product_on_page(){

    table_head.innerHTML="";
    table_body.innerHTML="";

    const tr=document.createElement('tr');
    tr.innerHTML=`
        <th>Name</th>
        <th>Model</th>
        <th>Core</th>
        <th>Operation</th>
   `
    table_head.appendChild(tr);

    products_database.forEach(product_single_array=>
        {    
            add_product(product_single_array.product_id,product_single_array.product_name, product_single_array.product_model, product_single_array.product_core); 
        });
}


function toggle_button(pressed_button) {
    if (pressed_button.innerText==='Add'){
        pressed_button.innerText="Remove";
        alert("Product Added to Cart");
    }else{
        pressed_button.innerText="Add";
        alert("Product Removed to Cart");
    }
    //Remove before Deploy
    console.log("Button Pressed: " + pressed_button.id);

    return pressed_button.id;
}



function start_job(){
    const button = document.getElementById('job_button');
    button.addEventListener('click',async()=>{
        try{
            const response=await fetch('/backend/background');
            const data=await response.json();

            job_result_list.push(data);
            console.log('Background Job: ',data);
            console.log(job_result_list);
        }catch(error){
            console.error('error calling background job')
        }
    });
}
start_job()

function job_table(result_list){
    table_head.innerHTML="";
    table_body.innerHTML="";

    job_result_list.forEach((item,index)=>{
        const tr=document.createElement("tr");
        tr.innerHTML=`
            <td>Job No: ${index}</td>
            <td>Job Input: ${item.input}</td>
            <td>Job Result: ${item.result}</td>
        ` 
        table_body.appendChild(tr);

    });
}

function fetch_cache(){
    const button=document.getElementById('show_cache');
    button.addEventListener('click',async()=>{
        try{
            const response=await fetch('/backend/cache');
            const data=await response.json();

            cache_list.push(data);
            console.log('Cache List: ',data);
            console.log(cache_list);
        }catch(error){
            console.error('error calling cache list');
        }
    });
}
fetch_cache();

function show_cache(a_cache_list){
    table_head.innerHTML="";
    table_body.innerHTML="";
    try{
        a_cache_list.forEach((item,index)=>{
        const tr=document.createElement("tr");
        tr.innerHTML=`
            <td>Cache No: ${index}</td>
            <td>Product Model: ${item.product_model}</td>
        `
        table_body.appendChild(tr);
        });
    }catch(error){
        alert(`Search Cache Empty`);
    }

}



document.querySelector('.link_container').addEventListener('click',function(event_captured){
    event_captured.preventDefault();

    // Switching Links

    switch (event_captured.target.id){

        case 'show_product':
            document.getElementById(event_captured.target.id).style.color="red"
            document.getElementById("show_cache").style.color="black"
            document.getElementById("show_jobs").style.color="black"
            show_product_on_page();
            break;

        case 'show_cache':
            document.getElementById(event_captured.target.id).style.color="red"
            document.getElementById("show_product").style.color="black"
            document.getElementById("show_jobs").style.color="black"
            show_cache(cache_list);
            break;

        case 'show_jobs':
            document.getElementById(event_captured.target.id).style.color="red"
            document.getElementById("show_product").style.color="black"
            document.getElementById("show_cache").style.color="black"
            job_table(job_result_list);
            break;

        default:
            console.log('unknown link clicked !!!');
            break;
    }
});