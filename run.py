#!/usr/bin/env python
# encoding: utf-8
"""


Created by bunnyman on 2013/10/19.
Copyright (c) 2013 Bunni.biz. All rights reserved.
"""


def main():
    from cardsubmitter import app
    app.config.from_object('config')
    app.run(debug=True)

if __name__ == '__main__':
    main()

__author__ = 'bunnyman'
