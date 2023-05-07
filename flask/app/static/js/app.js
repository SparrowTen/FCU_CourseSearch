// // 產出第一層
// var colleges = ["北", "中", "南"];

// var inner = "";
// for (var i = 0; i < colleges.length; i++) {
//   inner += `<option value=i>${colleges[i]}</option>`;
// }
// $("#list1").html(inner); //寫入
// var noIndex; //第二層的index
// //選擇第一層後，產出第二層
// var sectors = new Array();
// sectors[0] = ["台北 ", " 桃園", " 新竹"];
// sectors[1] = ["台中", "彰化", " 苗栗 "];
// sectors[2] = ["高雄 ", "屏東", " 台南 "];
// $("#list1").change(function () {
//   index = this.selectedIndex; //第一層的index
//   noIndex = index;
//   console.log("no1", this.selectedIndex);
//   console.log("第二層的長度", sectors[index].length); //第二層的長度
//   console.log("第二層選擇的陣列", sectors[index]); //第二層選擇的陣列
//   var Sinner = "";
//   for (var i = 0; i < sectors[index].length; i++) {
//     // Sinner=Sinner+'<option value=i>'+sectors[index][i]+'</option>';
//     Sinner += `<option value=i>${sectors[index][i]}</option>`;
//   }
//   $("#list2").html(Sinner);

//   // 第三層
//   var sectorss = new Array();
//   sectorss[0] = ["台北 ", " 桃園", " 新竹 "];
//   sectorss[1] = ["台中 ", " 彰化", " 苗栗 "];
//   sectorss[2] = ["高雄 ", "屏東 ", " 台南 "];

//   sectorss[0][0] = ["中山 ", " 松山", " 士林"];
//   sectorss[0][1] = ["中壢 ", " 內壢", " 楊梅"];
//   sectorss[0][2] = ["竹北 ", " 竹東", " 內灣"];
//   sectorss[1][0] = ["太平 ", " 大甲", " 清水"];
//   sectorss[1][1] = ["員林 ", " 田中", " 彰化"];
//   sectorss[1][2] = ["通宵 ", " 苑里", " 三義"];
//   sectorss[2][0] = ["鳳山 ", " 楠梓", " 鼓山"];
//   sectorss[2][1] = ["枋山 ", " 林邊", " 佳東"];
//   sectorss[2][2] = ["南科 ", " 永康", " 保安"];

//   console.log(sectorss);

//   $("#list2").change(function () {
//     index = this.selectedIndex;
//     console.log("no2", this.selectedIndex);
//     var Sinner3 = "";
//     console.log("0000", sectorss[noIndex]);
//     for (var i = 0; i < sectorss[noIndex][index].length; i++) {
//       Sinner3 =
//         Sinner3 +
//         "<option value=i>" +
//         sectorss[noIndex][index][i] +
//         "</option>";
//     }
//     $("#list3").html(Sinner3);
//   });

//   $("#list2").change();
// });
// $("#list1").change();

// $(document).ready(function () {
//   var colleges = [
//     "工程與科學學院",
//     "商學院",
//     "人社學院",
//     "資電學院",
//     "建設學院",
//     "金融學院",
//     "國際科技與管理學院",
//   ];

//   var inner = "";
//   for (var i = 0; i < colleges.length; i++) {
//     inner += `<option value=i>${colleges[i]}</option>`;
//   }
//   $("#college-list").html(inner);

//   var noIndex;
//   var sectors = new Array();
//   sectors[0] = [
//     "機電系",
//     "纖維複材系",
//     "工工系",
//     "化工系",
//     "航太系",
//     "精密系統設計學位學程",
//     "應數系",
//     "環科系",
//     "材料系",
//     "光電系",
//   ];
//   sectors[1] = [
//     "會計系",
//     "企管系",
//     "國際經營與貿易學系",
//     "財稅系",
//     "統計系",
//     "經濟系",
//     "合作經濟暨社會事業經營學系",
//     "行銷系",
//     "國企學士學程英語專班",
//   ];
//   sectors[2] = ["中文系", "外文系"];
//   sectors[3] = ["資訊系", "電子系", "電機系", "自控系", "通訊系"];
//   sectors[4] = ["土木系", "水利系", "運輸與物流學系", "都資系", "土管系"];
//   sectors[5] = [
//     "財金系",
//     "風保系",
//     "財務工程與精算學程",
//     "國際科技與管理學院",
//     "澳洲墨爾本皇家理工大學商學",
//     "電機資訊雙學士學位學程",
//     "商學大數據分析雙學士學位學",
//     "美國加州聖荷西州立大學工程",
//   ];

//   $("#college-list").change(function () {
//     function changeCollege(index) {
//       var Sinner = "";
//       for (var i = 0; i < sectors[index].length; i++) {
//         Sinner = Sinner + "<option value=i>" + sectors[index][i] + "</option>";
//       }
//       var sectorSelect = document.getElementById("sector-list");
//       sectorSelect.innerHTML = Sinner;
//     }
//     $("sector-list").html(Sinner);
//   });
// });
