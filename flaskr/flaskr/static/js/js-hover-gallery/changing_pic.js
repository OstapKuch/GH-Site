

		var IntervalID;
		var img;
		
		timeout()
		var a = 0;
		function timeout() {

			function change() {
				
				
				var image = document.getElementById("img-changed_"+a);
				var image_2 = document.getElementById("img-changed_"+(a+1));
				img = image.src;
				if(a==8){
				var image_2 = document.getElementById("img-changed_0");
				image.src = image_2.src;
				image.id = "img-changed_0";
				image.class = "all studio img-a-left1";
				

				image_2.src = img;
				image_2.id = "img-changed_"+a;
				image_2.class = "all studio img-a-left2";
				a=-1;
				

				} else {
				image.src = image_2.src;
				image.id = "img-changed_"+(a+1);
				image.class = "all studio img-a-left1";
				

				image_2.src = img;
				image_2.id = "img-changed_"+a;
				image_2.class = "all studio img-a-left2";

				}



				a++;
				

			}	IntervalID = setInterval(change, 4000);

		}

						
		


			


		
		function stop_1(clicked_id) {
			clearInterval(IntervalID);
			for(i=0; i<9;i++){
			var imag = "img-changed_"+i;
			if(clicked_id==imag){
				

				if(a==9) { a = 0;}	
				var image = document.getElementById("img-changed_"+a);
				var image_2 = document.getElementById(clicked_id);
				img = image.src;

				image.src = image_2.src;
				image.id = clicked_id;
				image.class = "all studio img-a-left1";


				image_2.src = img;
				image_2.id = "img-changed_"+a;
				image_2.class = "all studio img-a-left2";
				a=i;
				i=9;
				timeout()

				//alert(imag, clicked_id)
				
			}
			}
			
		}