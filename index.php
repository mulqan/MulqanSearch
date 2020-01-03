<?php
$search = isset($_GET['search']) ? $_GET['search'] : '';
$command = escapeshellcmd('python Query.py ' . $search);
$output = shell_exec($command);
$content = json_decode($output, true);
?>

<!doctype html>
<html lang="en">
  <head>
    <!-- Required meta tags -->
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

    <!-- Bootstrap CSS -->
    <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css">

    <title>Mulqan</title>
  </head>
  <body>
    <div class="jumbotron jumbotron-fluid">
      <div class="container">
        <h1 class="display-4 mb-3">Mulqan</h1>
        <form class="" action="" method="get">
          <div class="input-group mb-3">
            <input type="text" name="search" value="<?php echo $search; ?>" class="form-control form-control-lg" placeholder="Pencarian Sederhana" aria-label="Pencarian Sederhana" aria-describedby="button-addon2">
            <div class="input-group-append">
              <button class="btn btn-outline-secondary px-4" type="submit" id="button-addon2">Cari</button>
            </div>
          </div>
        </form>
      </div>
    </div>

    <div class="container">
      <?php for ($i=0; $i < count($content); $i++):?>
        <div class="card mb-3">
          <div class="card-body">
            <h5 class="card-title"><?php echo $content[$i]['title']; ?></h5>
            <h6 class="card-subtitle mb-2 text-muted"><?php echo $content[$i]['desc']; ?></h6>
            <p class="card-text"><?php echo $content[$i]['body']; ?></p>
            <a href="<?php echo $content[$i]['url']; ?>" class="card-link float-right">Lihat Halaman Asli</a>
          </div>
        </div>
      <?php endfor ?>
    </div>

    <!-- Optional JavaScript -->
    <!-- jQuery first, then Popper.js, then Bootstrap JS -->
    <script src="https://code.jquery.com/jquery-3.3.1.slim.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.14.7/umd/popper.min.js"></script>
    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/js/bootstrap.min.js"></script>
  </body>
</html>
