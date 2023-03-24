



# 文件格式

https://github.com/MichaelGrupp/evo/wiki/Formats#bag---ros-bagfile

# 绘制轨迹

https://github.com/MichaelGrupp/evo/wiki/evo_traj

# 评估位姿轨迹误差

https://github.com/MichaelGrupp/evo/wiki/Metrics

```python
logger.debug(SEP)
data = (traj_ref, traj_est)
ape_metric = metrics.APE(pose_relation)
ape_metric.process_data(data)
```

**轨迹对齐**

使用umeyama算法实现sim3变换

```python
def umeyama_alignment(x: np.ndarray, y: np.ndarray,
                      with_scale: bool = False) -> UmeyamaResult:
    """
    Computes the least squares solution parameters of an Sim(m) matrix
    that minimizes the distance between a set of registered points.
    Umeyama, Shinji: Least-squares estimation of transformation parameters
                     between two point patterns. IEEE PAMI, 1991
    :param x: mxn matrix of points, m = dimension, n = nr. of data points
    :param y: mxn matrix of points, m = dimension, n = nr. of data points
    :param with_scale: set to True to align also the scale (default: 1.0 scale)
    :return: r, t, c - rotation matrix, translation vector and scale factor
    """
```

主要命令

* `evo_traj` - tool for analyzing, plotting or exporting one or more trajectories
* `evo_res` - tool for comparing one or multiple result files from `evo_ape` or `evo_rpe`
* `evo_fig` - (experimental) tool for re-opening serialized plots (saved with `--serialize_plot`)
* `evo_config` - tool for global settings and config file manipulation

详细内容可参考readme.md

evo_ape tum pose1.txt pose2.txt --plot_mode xyz --align --save_plot ~/Desktop/evo/

evo_ape tum pose_gt.txt pose_t.txt --plot_mode xyz --align --correct_scale --save_plot ~/Desktop/evo/