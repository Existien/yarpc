/* Generated by YARPC
 * Version:  0.1.0
 * Definition:
 *   File: /workspace/tests/definitions/qt6/04_arrays.yml
 *   Template: qt6/types_source.j2
 */
#include "types.hpp"
#include <QList>
#include <QDBusMetaType>
#include <QJSValueIterator>

namespace gen::arrays {

void registerMetaTypes() {
    qRegisterMetaType<StructArray>("StructArray");
    qDBusRegisterMetaType<StructArray>();
    qRegisterMetaType<SimonsArray>("SimonsArray");
    qDBusRegisterMetaType<SimonsArray>();
    qRegisterMetaType<QList<QList<double>>>("QList<QList<double>>");
    qDBusRegisterMetaType<QList<QList<double>>>();
    qRegisterMetaType<QList<QList<QString>>>("QList<QList<QString>>");
    qDBusRegisterMetaType<QList<QList<QString>>>();
    qRegisterMetaType<QList<QList<uint>>>("QList<QList<uint>>");
    qDBusRegisterMetaType<QList<QList<uint>>>();
    qRegisterMetaType<QList<double>>("QList<double>");
    qDBusRegisterMetaType<QList<double>>();
    qRegisterMetaType<QList<SimonsArray>>("QList<SimonsArray>");
    qDBusRegisterMetaType<QList<SimonsArray>>();
    qRegisterMetaType<QList<QString>>("QList<QString>");
    qDBusRegisterMetaType<QList<QString>>();
    qRegisterMetaType<QList<StructArray>>("QList<StructArray>");
    qDBusRegisterMetaType<QList<StructArray>>();
    qRegisterMetaType<QList<uint>>("QList<uint>");
    qDBusRegisterMetaType<QList<uint>>();
}

bool operator!=(const QList<SimonsArray> &lhs, const QList<SimonsArray> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=0; i<lhs.size(); ++i) {
        if (lhs[i] != rhs[i]) {
            return true;
        }
    }
    return false;
}

bool operator!=(const QList<StructArray> &lhs, const QList<StructArray> &rhs) {
    if (lhs.size() != rhs.size()) {
        return true;
    }
    for (auto i=0; i<lhs.size(); ++i) {
        if (lhs[i] != rhs[i]) {
            return true;
        }
    }
    return false;
}

}