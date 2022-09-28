function Mudaestado(id){
	var disp = document.getElementById(id);
	if(disp.style.display == 'none'){
		disp.style.display = 'block'
	}else{
		disp.style.display = 'none'
	}

}

function GeraPDF(id){
	let container = document.getElementById(id)

	let opt = {
		margin: 1,
		filename: 'Servico_Saida_PDF.pdf',
		image: {type: 'jpg', quality: 0.98},
		html2canvas: {scale: 2},
	}

	html2pdf().set(opt).from(container).save()
}