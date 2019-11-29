var markers = new Array(); //현재 생성된 마커정보를 담아둠

var basket_hidden = document.getElementById("basket_hidden").textContent;
var coor = basket_hidden.split('|');
var coor_list = new Array();
for (var i = 0, len = coor.length; i<len-1; i+=3) {
    coor_list.push({"title":coor[i], "x_coor":coor[i+1], "y_coor":coor[i+2]});
}

//for (var i = 0, len = coor.length; i<len-1; i++) {
    //alert(coor_list[i]["title"]+coor_list[i]["x_coor"]+coor_list[i]["y_coor"]);

//}

var MARKER_WIDTH = 33, // 기본, 클릭 마커의 너비
    MARKER_HEIGHT = 36, // 기본, 클릭 마커의 높이
    OFFSET_X = 12, // 기본, 클릭 마커의 기준 X좌표
    OFFSET_Y = MARKER_HEIGHT, // 기본, 클릭 마커의 기준 Y좌표
    OVER_MARKER_WIDTH = 40, // 오버 마커의 너비
    OVER_MARKER_HEIGHT = 42, // 오버 마커의 높이
    OVER_OFFSET_X = 13, // 오버 마커의 기준 X좌표
    OVER_OFFSET_Y = OVER_MARKER_HEIGHT, // 오버 마커의 기준 Y좌표
    SPRITE_MARKER_URL = 'http://t1.daumcdn.net/localimg/localimages/07/mapapidoc/markers_sprites2.png', // 스프라이트 마커 이미지 URL
    SPRITE_WIDTH = 126, // 스프라이트 이미지 너비
    SPRITE_HEIGHT = 146, // 스프라이트 이미지 높이
    SPRITE_GAP = 10; // 스프라이트 이미지에서 마커간 간격

var markerSize = new kakao.maps.Size(MARKER_WIDTH, MARKER_HEIGHT), // 기본, 클릭 마커의 크기
    markerOffset = new kakao.maps.Point(OFFSET_X, OFFSET_Y), // 기본, 클릭 마커의 기준좌표
    overMarkerSize = new kakao.maps.Size(OVER_MARKER_WIDTH, OVER_MARKER_HEIGHT), // 오버 마커의 크기
    overMarkerOffset = new kakao.maps.Point(OVER_OFFSET_X, OVER_OFFSET_Y), // 오버 마커의 기준 좌표
    spriteImageSize = new kakao.maps.Size(SPRITE_WIDTH, SPRITE_HEIGHT); // 스프라이트 이미지의 크기

var positions = [];
var selectedMarker = null; // 클릭한 마커를 담을 변수

for (var i = 0, len = coor_list.length; i<len; i++) {
  positions.push(
    {
        'title': coor_list[i]['title'], 
        'latlng': new kakao.maps.LatLng(coor_list[i]["x_coor"], coor_list[i]["y_coor"])
    }
    );
}


var mapContainer = document.getElementById('map'), // 지도를 표시할 div
    mapOption = { 
        center: new kakao.maps.LatLng(37.465262, 126.810566), // 지도의 중심좌표
        level: 9 // 지도의 확대 레벨
    };

var map = new kakao.maps.Map(mapContainer, mapOption); // 지도를 생성합니다

// 일반 지도와 스카이뷰로 지도 타입을 전환할 수 있는 지도타입 컨트롤을 생성합니다
var mapTypeControl = new kakao.maps.MapTypeControl();
// 지도 타입 컨트롤을 지도에 표시, TOPRIGHT는 오른쪽 위를 의미한다.
map.addControl(mapTypeControl, kakao.maps.ControlPosition.TOPRIGHT);
// 지도 확대 축소를 제어할 수 있는  줌 컨트롤을 생성합니다
var zoomControl = new kakao.maps.ZoomControl();
map.addControl(zoomControl, kakao.maps.ControlPosition.RIGHT);

// 키보드의 방향키와 +,-키로 지도 이동,확대,축소 가능여부를 설정
map.setKeyboardShortcuts(true);



// 지도 위에 마커를 표시합니다
for (var i = 0, len = positions.length; i < len; i++) {
    var gapX = (MARKER_WIDTH + SPRITE_GAP), // 스프라이트 이미지에서 마커로 사용할 이미지 X좌표 간격 값
        originY = (MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 기본, 클릭 마커로 사용할 Y좌표 값
        overOriginY = (OVER_MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 오버 마커로 사용할 Y좌표 값
        normalOrigin = new kakao.maps.Point(0, originY), // 스프라이트 이미지에서 기본 마커로 사용할 영역의 좌상단 좌표
        clickOrigin = new kakao.maps.Point(gapX, originY), // 스프라이트 이미지에서 마우스오버 마커로 사용할 영역의 좌상단 좌표
        overOrigin = new kakao.maps.Point(gapX * 2, overOriginY); // 스프라이트 이미지에서 클릭 마커로 사용할 영역의 좌상단 좌표
        
    // 마커를 생성하고 지도위에 표시합니다
    addMarker(positions[i]['latlng'], positions[i]['title'] , normalOrigin, overOrigin, clickOrigin);
}

// 마커를 생성하고 지도 위에 표시하고, 마커에 mouseover, mouseout, click 이벤트를 등록하는 함수입니다
function addMarker(position, titles,normalOrigin, overOrigin, clickOrigin) {
    // 기본 마커이미지, 오버 마커이미지, 클릭 마커이미지를 생성합니다
    var normalImage = createMarkerImage(markerSize, markerOffset, normalOrigin),
        overImage = createMarkerImage(overMarkerSize, overMarkerOffset, overOrigin),
        clickImage = createMarkerImage(markerSize, markerOffset, clickOrigin);
    
    // 마커를 생성하고 이미지는 기본 마커 이미지를 사용합니다
    var marker = new kakao.maps.Marker({
        map: map,
        position: position,
        title : titles,
        image: normalImage
    });
    markers.push(marker);

    // 마커 객체에 마커아이디와 마커의 기본 이미지를 추가합니다
    marker.normalImage = normalImage;

    // 마커에 mouseover 이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'mouseover', function() {
        // 클릭된 마커가 없고, mouseover된 마커가 클릭된 마커가 아니면
        // 마커의 이미지를 오버 이미지로 변경합니다
        if (!selectedMarker || selectedMarker !== marker) {
            marker.setImage(overImage);
        }
    });

    // 마커에 mouseout 이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'mouseout', function() {
        // 클릭된 마커가 없고, mouseout된 마커가 클릭된 마커가 아니면
        // 마커의 이미지를 기본 이미지로 변경합니다
        if (!selectedMarker || selectedMarker !== marker) {
            marker.setImage(normalImage);
        }
    });

    // 마커에 click 이벤트를 등록합니다
    kakao.maps.event.addListener(marker, 'click', function() {
            // 클릭된 마커 객체가 null이 아니면
            // 클릭된 마커의 이미지를 기본 이미지로 변경하고
            !!selectedMarker && selectedMarker.setImage(selectedMarker.normalImage);
            // 현재 클릭된 마커의 이미지는 클릭 이미지로 변경합니다
            marker.setImage(clickImage);
            //alert(marker.mc);
            //console.log(marker);
            var modal_title = document.getElementById("modal_title");
            //modal_title.innerHTML = titles;
            
            titles = titles.replace( /(\s*)/g, "");

            $("#modal_button").attr("data-target","#"+titles);
            //alert($("#modal_button").attr("data-target"));
            modal_button.click();
        

            // 클릭된 마커를 현재 클릭된 마커 객체로 설정합니다
            selectedMarker = marker;
    });
}



// MakrerImage 객체를 생성하여 반환하는 함수입니다
function createMarkerImage(markerSize, offset, spriteOrigin) {
    var markerImage = new kakao.maps.MarkerImage(
        SPRITE_MARKER_URL, // 스프라이트 마커 이미지 URL
        markerSize, // 마커의 크기
        {
            offset: offset, // 마커 이미지에서의 기준 좌표
            spriteOrigin: spriteOrigin, // 스트라이프 이미지 중 사용할 영역의 좌상단 좌표
            spriteSize: spriteImageSize // 스프라이트 이미지의 크기
        }
    );    
    return markerImage;
}



function ajax_change_marker(id) {
    //이전 마커들 삭제
    for (var i = 0; i < markers.length; i++) {
        markers[i].setMap(null);
    }

    var hidden = document.getElementById(id).textContent;
    var coor = hidden.split('|');
    var coor_list = new Array();
    for (var i = 0, len = coor.length; i<len-1; i+=3) {
        coor_list.push({"title":coor[i], "x_coor":coor[i+1], "y_coor":coor[i+2]});
    }

    var positions = [];
    var selectedMarker = null; // 클릭한 마커를 담을 변수
    
    for (var i = 0, len = coor_list.length; i<len; i++) {
      positions.push(
        {
            'title': coor_list[i]['title'], 
            'latlng': new kakao.maps.LatLng(coor_list[i]["x_coor"], coor_list[i]["y_coor"])
        }
        );
    }

    // 지도 위에 마커를 표시합니다
    for (var i = 0, len = positions.length; i < len; i++) {
        var gapX = (MARKER_WIDTH + SPRITE_GAP), // 스프라이트 이미지에서 마커로 사용할 이미지 X좌표 간격 값
            originY = (MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 기본, 클릭 마커로 사용할 Y좌표 값
            overOriginY = (OVER_MARKER_HEIGHT + SPRITE_GAP) * i, // 스프라이트 이미지에서 오버 마커로 사용할 Y좌표 값
            normalOrigin = new kakao.maps.Point(0, originY), // 스프라이트 이미지에서 기본 마커로 사용할 영역의 좌상단 좌표
            clickOrigin = new kakao.maps.Point(gapX, originY), // 스프라이트 이미지에서 마우스오버 마커로 사용할 영역의 좌상단 좌표
            overOrigin = new kakao.maps.Point(gapX * 2, overOriginY); // 스프라이트 이미지에서 클릭 마커로 사용할 영역의 좌상단 좌표
            
        // 마커를 생성하고 지도위에 표시합니다
        addMarker(positions[i]['latlng'], positions[i]['title'] , normalOrigin, overOrigin, clickOrigin);
    }

}

