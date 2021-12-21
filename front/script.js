let state = {
    isTranslatingTo: true,
    swapLang: ()=>{
        state.isTranslatingTo = !state.isTranslatingTo;
        const to = document.querySelector('#to').innerText;
        const from = document.querySelector('#from').innerText;
        document.querySelector('#to').innerText = from;
        document.querySelector('#from').innerText = to;
        clear()
    }
}

async function translate(){
    const input = document.querySelector('#textarea');
    const output = document.querySelector('.output');
    output.classList.add('outputChange');
    if(state.isTranslatingTo)
        output.innerText = await eel.translate_to(input.value)();
    else output.innerText = await eel.translate_from(input.value)();
    document.querySelector(".copy").classList.add('copyVisible');
    if(input.value === '')
        clear();
}
function clear(){
    document.querySelector('#textarea').value = '';
    document.querySelector('.output').innerText = 'Перевод';
    document.querySelector('.output').classList.remove('outputChange');
    document.querySelector(".copy").classList.remove('copyVisible');
}

document.querySelector('.change').addEventListener('click', state.swapLang);
document.querySelector('textarea').addEventListener('input', translate);
document.querySelector('.copy').addEventListener('click', async ()=>{
    const outputValue = document.querySelector('.output').innerText;
    await eel.copy(outputValue);
})