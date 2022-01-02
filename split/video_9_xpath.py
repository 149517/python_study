from lxml import etree

html = """
    <body>	
		<div id="navigation">
			<ul type="none" id="nav_ul">
				<img src="img/lv_logo.png" alt="logo" id="logo" style="float: left;">
				<li>首页</li>
				<li>前端入门</li>
				<li class="bb">前端进阶</li>
				<li>站长的书</li>
				<li>高校版块</li>
				<li>学习路线</li>
				<li>在线测试</li>
			</ul>
		</div>		
		<div id="round">
			<img src="img/lunbotu_1.jpg"/>
			<img src="img/lunbotu_2.jpg"/>
		</div>
	</body>

"""
et = etree.HTML(html)
result = et.xpath('./body/div/ul/li[@class="bb"]/text()')
print(result)