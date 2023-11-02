var Links = {
    LinkSetColor:function (color){
    var a_selector = document.querySelectorAll('a');
    var i=0;
    while(i<a_selector.length){
        a_selector[i].style.color = color;
        i += 1;
      }
    }
  }

  var Body = {
    setColor:function (color){
      document.querySelector('body').style.color = color;
    },
    setBackground:function (color){
      document.querySelector('body').style.backgroundColor = color;
    }
  }

  function day_night(self){
    if(self.value === 'day'){
      Body.setColor('black');
      Body.setBackground('white');
      self.value = 'night';
      Links.LinkSetColor('red');
    }
    else{
      Body.setColor('white');
      Body.setBackground('black');
      self.value = 'day';
      Links.LinkSetColor('white');
    }
  }