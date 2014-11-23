# Reverse Subtitles Punctuation

This project is a small python script for reversing the punctuation of an SRT subtitle. It is based on the Subtitle Workshop 2.61 feature with the same capabilities.

## Motivation

When I use any media streamer to stream movies to my TV, usually the Hebrew subtitles have reversed puncuation. This is due RTL nature of the hebrew language. This can drive me crazy, but than again, it is not easy to support RTL languages.

## Installation & Usage

1. Install Python, 2.6 or above, in case you don't have it yet.
2. run:
    ```sh
    $ python rev.py <SRT_FILE>
    ```
3. If you want to create Context-Menu shortcut, run create_registry_file.py and run add_to_reg.reg. Note: this will only work if you not move the rev.py file. Run the create_registry_file.py at your final foalder. Also, you still need python installed.

## Contributing

Want to add new features?

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request [here](https://github.com/asafs/reverse-subtitles/pulls)

Found a but or want to request a new feature?
1. go [here](https://github.com/asafs/reverse-subtitles/pulls)


## History

no version yet :(

## License

See LICENCE file