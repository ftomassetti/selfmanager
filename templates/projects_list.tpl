<html>
<body>
<ul>
%for p in projects:
	<li>{{p.id}} - {{p.title}}</li>
%end
</ul>
</body>
</html>