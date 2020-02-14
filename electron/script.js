var isSecond = 1;
    function cat_str(string)
    {
      input_box.value += string;
    }

    function del()
    {
      input_box.value = input_box.value.slice(0, -1);
    }

    function clear_input()
    {
      input_box.value = '';
    }

    function second()
    {
      if (isSecond == 1)
      {
        document.querySelector('#btn1_1').innerHTML = 'sin<sup>-1</sup>';
        document.querySelector('#btn1_2').innerHTML = 'cos<sup>-1</sup>';
        document.querySelector('#btn1_3').innerHTML = 'tan<sup>-1</sup>';
        document.querySelector('#btn1_4').textContent = 'del';
        document.querySelector('#btn1_5').textContent = 'clear';
        document.querySelector('#btn2_1').textContent = '1';
        document.querySelector('#btn2_2').textContent = '2';
        document.querySelector('#btn2_3').textContent = '3';
        document.querySelector('#btn2_4').textContent = 'log';
        document.querySelector('#btn2_5').textContent = 'ln';
        document.querySelector('#btn3_1').textContent = '4';
        document.querySelector('#btn3_2').textContent = '5';
        document.querySelector('#btn3_3').textContent = '6';
        document.querySelector('#btn3_4').textContent = 'π';
        document.querySelector('#btn3_5').textContent = 'e';
        document.querySelector('#btn4_1').textContent = '7';
        document.querySelector('#btn4_2').textContent = '8';
        document.querySelector('#btn4_3').textContent = '9';
        document.querySelector('#btn4_4').textContent = 'F<->D';
        document.querySelector('#btn4_5').textContent = '√';
        document.querySelector('#btn5_1').textContent = '0';
        document.querySelector('#btn5_2').textContent = '.';
        document.querySelector('#btn5_3').textContent = '^';
        document.querySelector('#btn5_4').textContent = '2nd';
        document.querySelector('#btn5_5').textContent = '=';

        document.querySelector('#btn1_1').setAttribute("onclick", "javascript:cat_str('arcsin(');");
        document.querySelector('#btn1_2').setAttribute("onclick", "javascript:cat_str('arccos(');");
        document.querySelector('#btn1_3').setAttribute("onclick", "javascript:cat_str('arctan(');");
        document.querySelector('#btn1_4').setAttribute("onclick", "javascript:del();");
        document.querySelector('#btn1_5').setAttribute("onclick", "javascript:clear_input();");
        document.querySelector('#btn2_1').setAttribute("onclick", "javascript:cat_str('1');");
        document.querySelector('#btn2_2').setAttribute("onclick", "javascript:cat_str('2');");
        document.querySelector('#btn2_3').setAttribute("onclick", "javascript:cat_str('3');");
        document.querySelector('#btn2_4').setAttribute("onclick", "javascript:cat_str('log(');");
        document.querySelector('#btn2_5').setAttribute("onclick", "javascript:cat_str('ln(');");
        document.querySelector('#btn3_1').setAttribute("onclick", "javascript:cat_str('4');");
        document.querySelector('#btn3_2').setAttribute("onclick", "javascript:cat_str('5');");
        document.querySelector('#btn3_3').setAttribute("onclick", "javascript:cat_str('6');");
        document.querySelector('#btn3_4').setAttribute("onclick", "javascript:cat_str('π');");
        document.querySelector('#btn3_5').setAttribute("onclick", "javascript:cat_str('e');");
        document.querySelector('#btn4_1').setAttribute("onclick", "javascript:cat_str('7');");
        document.querySelector('#btn4_2').setAttribute("onclick", "javascript:cat_str('8');");
        document.querySelector('#btn4_3').setAttribute("onclick", "javascript:cat_str('9');");
        document.querySelector('#btn4_4').setAttribute("onclick", "javascript:f_to_d();");
        document.querySelector('#btn4_5').setAttribute("onclick", "javascript:cat_str('√(');");
        document.querySelector('#btn5_1').setAttribute("onclick", "javascript:cat_str('0');");
        document.querySelector('#btn5_2').setAttribute("onclick", "javascript:cat_str('.');");
        document.querySelector('#btn5_3').setAttribute("onclick", "javascript:cat_str('^');");
        document.querySelector('#btn5_4').setAttribute("onclick", "javascript:second();");
        document.querySelector('#btn5_5').setAttribute("onclick", "javascript:evaluate_input();");
        document.getElementById("btn5_4").style.backgroundColor = "#141615";
      }
      else 
      {
        document.querySelector('#btn1_1').textContent = 'sin';
        document.querySelector('#btn1_2').textContent = 'cos';
        document.querySelector('#btn1_3').textContent = 'tan';
        document.querySelector('#btn1_4').textContent = 'del';
        document.querySelector('#btn1_5').textContent = 'clear';
        document.querySelector('#btn2_1').textContent = '1';
        document.querySelector('#btn2_2').textContent = '2';
        document.querySelector('#btn2_3').textContent = '3';
        document.querySelector('#btn2_4').textContent = '(';
        document.querySelector('#btn2_5').textContent = ')';
        document.querySelector('#btn3_1').textContent = '4';
        document.querySelector('#btn3_2').textContent = '5';
        document.querySelector('#btn3_3').textContent = '6';
        document.querySelector('#btn3_4').textContent = '*';
        document.querySelector('#btn3_5').textContent = '+';
        document.querySelector('#btn4_1').textContent = '7';
        document.querySelector('#btn4_2').textContent = '8';
        document.querySelector('#btn4_3').textContent = '9';
        document.querySelector('#btn4_4').textContent = '/';
        document.querySelector('#btn4_5').textContent = '-';
        document.querySelector('#btn5_1').textContent = '0';
        document.querySelector('#btn5_2').textContent = '.';
        document.querySelector('#btn5_3').textContent = '^';
        document.querySelector('#btn5_4').textContent = '2nd';
        document.querySelector('#btn5_5').textContent = '=';

        document.querySelector('#btn1_1').setAttribute("onclick", "javascript:cat_str('sin(');");
        document.querySelector('#btn1_2').setAttribute("onclick", "javascript:cat_str('cos(');");
        document.querySelector('#btn1_3').setAttribute("onclick", "javascript:cat_str('tan(');");
        document.querySelector('#btn1_4').setAttribute("onclick", "javascript:del();");
        document.querySelector('#btn1_5').setAttribute("onclick", "javascript:clear_input();");
        document.querySelector('#btn2_1').setAttribute("onclick", "javascript:cat_str('1');");
        document.querySelector('#btn2_2').setAttribute("onclick", "javascript:cat_str('2');");
        document.querySelector('#btn2_3').setAttribute("onclick", "javascript:cat_str('3');");
        document.querySelector('#btn2_4').setAttribute("onclick", "javascript:cat_str('(');");
        document.querySelector('#btn2_5').setAttribute("onclick", "javascript:cat_str(')');");
        document.querySelector('#btn3_1').setAttribute("onclick", "javascript:cat_str('4');");
        document.querySelector('#btn3_2').setAttribute("onclick", "javascript:cat_str('5');");
        document.querySelector('#btn3_3').setAttribute("onclick", "javascript:cat_str('6');");
        document.querySelector('#btn3_4').setAttribute("onclick", "javascript:cat_str('*');");
        document.querySelector('#btn3_5').setAttribute("onclick", "javascript:cat_str('+');");
        document.querySelector('#btn4_1').setAttribute("onclick", "javascript:cat_str('7');");
        document.querySelector('#btn4_2').setAttribute("onclick", "javascript:cat_str('8');");
        document.querySelector('#btn4_3').setAttribute("onclick", "javascript:cat_str('9');");
        document.querySelector('#btn4_4').setAttribute("onclick", "javascript:cat_str('/');");
        document.querySelector('#btn4_5').setAttribute("onclick", "javascript:cat_str('-');");
        document.querySelector('#btn5_1').setAttribute("onclick", "javascript:cat_str('0');");
        document.querySelector('#btn5_2').setAttribute("onclick", "javascript:cat_str('.');");
        document.querySelector('#btn5_3').setAttribute("onclick", "javascript:cat_str('^');");
        document.querySelector('#btn5_4').setAttribute("onclick", "javascript:second();");
        document.querySelector('#btn5_5').setAttribute("onclick", "javascript:evaluate_input();");
        document.getElementById("btn5_4").style.backgroundColor = "#1d211f";

      }

      isSecond *= -1;
      

    }
    
    function evaluate_input()
    {
      var input_string = document.getElementById("input_box").value;
      const execSync = require('child_process').execSync;
      var shellCommand = "python ../calc_files/calculation.py -e " + input_string;
      const cmd = execSync(shellCommand, { encoding: 'utf-8' });  // the default is 'buffer'

      const fs = require('fs');
      path = require('path');    
      var output;
      filePath = path.join(__dirname, '../log/previous_calculations.txt');
      fs.readFile(filePath, (err, data) => { 
        if (err) throw err; 
        output = data.toString().split(',');
        output = output[output.length-1];
        document.getElementById("input_box").value = output;
      });
    }

    function f_to_d()
    {
      var input_string = document.getElementById("input_box").value;
      const execSync = require('child_process').execSync;
      var shellCommand = "python ../calc_files/f_to_d.py " + input_string;
      const cmd = execSync(shellCommand, { encoding: 'utf-8' });  // the default is 'buffer'

      const fs = require('fs');
      path = require('path');    
      var output;
      filePath = path.join(__dirname, '../log/previous_calculations.txt');
      fs.readFile(filePath, (err, data) => { 
        if (err) throw err; 
        output = data.toString().split(',');
        output = output[output.length-1];
        document.getElementById("input_box").value = output;
      });
    }

    setInterval(function(){
      var focusbox;
      focusbox = document.getElementById("input_box");
      focusbox.focus();
    });