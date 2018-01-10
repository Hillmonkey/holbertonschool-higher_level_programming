#!/usr/bin/node
'use strict';

if (process.argv.length !== 5) {
  console.log('incorrect number of arguments');
} else {
  let f1 = process.argv[2];
  let f2 = process.argv[3];
  let tgt = process.argv[4];

  /*
  let cp = require('child_process');
  let concat = cp.spawn('ls', ['-lsa']);
  */

  let exec = require('child_process');
  let child = exec.spawn('cat', [f1, f2 + ' > ' + tgt,
    function (error, stdout, stderr) {
      console.log('stdout: ' + stdout);
      console.log('stderr: ' + stderr);
        if (error !== null) {
          console.log('exec error: ' + error);
        }
    });
    child();
}
