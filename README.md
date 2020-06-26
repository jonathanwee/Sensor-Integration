# Sensor-Integration

Combination of Terabee ToF and NeoSpectra Spectrography.

Terabee Tof:
-SpectraMain      : To call all packets
-moduleNeoSpectra : Packet information. Refer to SDK page 23
-serverBluetooth  : Not in use

Spectrography:
-main.py              : Captures and streams img from display_depth_frame
-display_depth_frame  : Streams depth, scale_factor and colour_map can be changed
-get_centre_distance  : Distance capture
