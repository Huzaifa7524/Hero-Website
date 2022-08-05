$(".filter_dropdown_input").click(function(){
    var $this = $(this);
    var category_div=$this.siblings('#filter_category').val()
    $.ajax({ 
          method: "POST",
          url: `/filter_videos_home/`,
          data: {
        'filter_category': $this.siblings('#filter_category').val(),
        'filter': $this.text(),
       
        
      },
          success:function(response){
            $('.'+category_div).html("")
            console.log('save response', response)
            
            
            
      
          },
          error:function(){
              console.log('save url is not working')
          }
        });
});