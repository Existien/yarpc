/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/05_dicts.yml
 *   Template: qt6/types_source.j2
 */
#include "types.hpp"
#include <QList>
#include <QDBusMetaType>

void gen::dicts::registerMetaTypes() {
    qRegisterMetaType<StructDict>("StructDict");
    qDBusRegisterMetaType<StructDict>();
    qRegisterMetaType<SimonsDict>("SimonsDict");
    qDBusRegisterMetaType<SimonsDict>();
    qRegisterMetaType<QMap<QString, QString>>("QMap<QString, QString>");
    qDBusRegisterMetaType<QMap<QString, QString>>();
    qRegisterMetaType<QMap<QString, StructDict>>("QMap<QString, StructDict>");
    qDBusRegisterMetaType<QMap<QString, StructDict>>();
    qRegisterMetaType<QMap<QString, uint>>("QMap<QString, uint>");
    qDBusRegisterMetaType<QMap<QString, uint>>();
    qRegisterMetaType<QMap<QString, QMap<QString, uint>>>("QMap<QString, QMap<QString, uint>>");
    qDBusRegisterMetaType<QMap<QString, QMap<QString, uint>>>();
    qRegisterMetaType<QMap<QString, SimonsDict>>("QMap<QString, SimonsDict>");
    qDBusRegisterMetaType<QMap<QString, SimonsDict>>();
    qRegisterMetaType<QMap<QString, StructDict>>("QMap<QString, StructDict>");
    qDBusRegisterMetaType<QMap<QString, StructDict>>();
    qRegisterMetaType<QMap<QString, uint>>("QMap<QString, uint>");
    qDBusRegisterMetaType<QMap<QString, uint>>();
}

bool gen::dicts::operator!=(const QMap<QString, StructDict> &lhs, const QMap<QString, StructDict> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=lhs.keyBegin(); i!=lhs.keyEnd(); ++i) {
        if (!rhs.contains(*i))
        {
            return true;
        }
        if (lhs[*i] != rhs[*i]) {
            return true;
        }
    }
    return false;
}

bool gen::dicts::operator!=(const QMap<QString, SimonsDict> &lhs, const QMap<QString, SimonsDict> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=lhs.keyBegin(); i!=lhs.keyEnd(); ++i) {
        if (!rhs.contains(*i))
        {
            return true;
        }
        if (lhs[*i] != rhs[*i]) {
            return true;
        }
    }
    return false;
}
